import reflex as rx
from cve.state.base import State
from fastapi.exceptions import HTTPException
from typing import List
import httpx
from httpx import ReadTimeout
import pandas as pd

class QueryState(State):
    tipo : str
    plataforma : str
    nombre_version : str
    version_esp : str
    id_cve : str
    clasificacion : str
    id_cwe : str
    id_cve_change : str
    
    cpe : List[dict] = []
    
    data : List[dict] = []
    
    dataForTable = pd.read_csv("au.csv")
    
    def update_cpe(self, value):
        self.cpe = value
    
    def update_cve(self, value):
        self.data = value
        
    def update_clas(self, value):
        self.data = value
        return self.data
    
    def update_cwe(self, value):
        self.data = value
        
    def update_change(self, value):
        self.change = value
    
    def get_cves(self):
        return self.cpe
    
    def update_flagg(self, value):
        self.flagg = value
    
    def get_flag(self):
        return self.flagg
    
    @property
    def url_query(self):
        return f"cpeName=cpe:2.3:{self.tipo}:{self.plataforma}:{self.nombre_version}:{self.version_esp}:*:*:*:*:*:*:*"
    
    async def get_cpe(self):
        if not self.tipo or not self.plataforma or not self.nombre_version or not self.version_esp:
            return rx.window_alert("Todos los campos son requeridos.")
        try:                
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0/?{self.url_query}"

            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                
                if response.status_code == 200:
                    cve_data = response.json()
                    cve_items = cve_data.get("vulnerabilities", [])

                    top_5_cves = []
                    
                    for cve_item in cve_items[:5]:
                        cve_id = cve_item.get('cve', {}).get('id', '')
                        published_date = cve_item.get('cve', {}).get('published', '')
                        description = cve_item.get('cve', {}).get('descriptions', [{}])[0].get('value', '')
                        cvss_score = cve_item.get('cve', {}).get('metrics', {}).get('cvssMetricV2', [{}])[0].get('cvssData', {}).get('baseScore', '')

                        top_5_cves.append({
                            'cve_id': cve_id,
                            'published_date': published_date,
                            'description': description,
                            'cvss_score': cvss_score,
                        })
                    self.update_cpe(top_5_cves)
                    datList = self.cpe
                    df = pd.DataFrame(datList)     
                    df.to_csv("test.csv")
                    self.dataForTable = pd.read_csv("test.csv")
                else:
                    raise HTTPException(status_code=response.status_code, detail="Error en la solicitud HTTP")

        except ReadTimeout as e:
            print(f"Excepción de tiempo de espera de lectura durante la solicitud HTTP: {e}")
            
        except Exception as e:
            # Imprime la excepción para obtener más detalles
            print(f"Excepción durante la solicitud HTTP: {e}")
            raise HTTPException(status_code=500, detail=f"Error en la solicitud HTTP: {str(e)}")
    
    
    async def get_by_id(self):
        if not self.id_cve:
            return rx.window_alert("Campo requerido.")
        try:                
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0/?cveId={self.id_cve}"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                data = []

                if response.status_code == 200:
                    cve_info = response.json().get('vulnerabilities', [])

                    for vulnerability in cve_info:
                        cve_data = vulnerability.get('cve', {})
                        descriptions = cve_data.get('descriptions', [])
                        cvss_v2 = cve_data.get('metrics', {}).get('cvssMetricV2', [])

                    data.append({
                        'cve_id': cve_data.get('id', ''),
                        'published_date': cve_data.get('published', ''),
                        'description': descriptions[0].get('value', '') if descriptions else '',
                        'cvss_score': cvss_v2[0].get('cvssData', {}).get('baseScore', '') if cvss_v2 else '',
                    })
                    self.update_cve(data)
                    datList = self.data
                    df = pd.DataFrame(datList)     
                    df.to_csv("test.csv")
                    self.dataForTable = pd.read_csv("test.csv")
                else:
                    raise HTTPException(status_code=response.status_code, detail="Error en la solicitud HTTP")

        except ReadTimeout as e:
            print(f"Excepción de tiempo de espera de lectura durante la solicitud HTTP: {e}")
            
        except Exception as e:
            # Imprime la excepción para obtener más detalles
            print(f"Excepción durante la solicitud HTTP: {e}")
            raise HTTPException(status_code=500, detail=f"Error en la solicitud HTTP: {str(e)}")    
        
    
    async def get_classification(self):
        if not self.clasificacion:
            return rx.window_alert("Campo requerido.")
        try:                
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV3Severity={self.clasificacion}"
            print(url)
            async with httpx.AsyncClient() as client:
                response = await client.get(url)

                if response.status_code == 200:
                    cve_data = response.json()
                    cve_items = cve_data.get("vulnerabilities", [])

                    top_5_cves = []
                    
                    for cve_item in cve_items[:5]:
                        cve_id = cve_item.get('cve', {}).get('id', '')
                        published_date = cve_item.get('cve', {}).get('published', '')
                        description = cve_item.get('cve', {}).get('descriptions', [{}])[0].get('value', '')
                        cvss_score = cve_item.get('cve', {}).get('metrics', {}).get('cvssMetricV2', [{}])[0].get('cvssData', {}).get('baseScore', '')

                        top_5_cves.append({
                            'cve_id': cve_id,
                            'published_date': published_date,
                            'description': description,
                            'cvss_score': cvss_score,
                        })
                    self.update_clas(top_5_cves)
                    datList = self.data
                    df = pd.DataFrame(datList)     
                    df.to_csv("test.csv")
                    self.dataForTable = pd.read_csv("test.csv")
                else:
                    raise HTTPException(status_code=response.status_code, detail="Error en la solicitud HTTP")

        except ReadTimeout as e:
            print(f"Excepción de tiempo de espera de lectura durante la solicitud HTTP: {e}")
            
        except Exception as e:
            # Imprime la excepción para obtener más detalles
            print(f"Excepción durante la solicitud HTTP: {e}")
            raise HTTPException(status_code=500, detail=f"Error en la solicitud HTTP: {str(e)}") 
            
    
    async def get_cwe(self):
        if not self.id_cwe:
            return rx.window_alert("Campo requerido.")
        try:                
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cweId={self.id_cwe}"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)

                if response.status_code == 200:
                    cve_data = response.json()
                    cve_items = cve_data.get("vulnerabilities", [])

                    top_5_cves = []
                    
                    for cve_item in cve_items[:5]:
                        cve_id = cve_item.get('cve', {}).get('id', '')
                        published_date = cve_item.get('cve', {}).get('published', '')
                        description = cve_item.get('cve', {}).get('descriptions', [{}])[0].get('value', '')
                        cvss_score = cve_item.get('cve', {}).get('metrics', {}).get('cvssMetricV2', [{}])[0].get('cvssData', {}).get('baseScore', '')

                        top_5_cves.append({
                            'cve_id': cve_id,
                            'published_date': published_date,
                            'description': description,
                            'cvss_score': cvss_score,
                        })
                    self.update_cwe(top_5_cves)
                    datList = self.data
                    df = pd.DataFrame(datList)     
                    df.to_csv("test.csv")
                    self.dataForTable = pd.read_csv("test.csv")
                else:
                    raise HTTPException(status_code=response.status_code, detail="Error en la solicitud HTTP")

        except ReadTimeout as e:
            print(f"Excepción de tiempo de espera de lectura durante la solicitud HTTP: {e}")
        
        except Exception as e:
            # Imprime la excepción para obtener más detalles
            print(f"Excepción durante la solicitud HTTP: {e}")
            raise HTTPException(status_code=500, detail=f"Error en la solicitud HTTP: {str(e)}")
        
    def clear (self):
        self.id_cve = ""
        self.tipo = ""
        self.plataforma = ""
        self.nombre_version = ""
        self.version_esp = ""
        self.clasificacion = ""
        self.id_cwe = ""
        self.id_cve_change = ""
        self.dataForTable = pd.read_csv("au.csv")