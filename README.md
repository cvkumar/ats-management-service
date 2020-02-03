# ats-management-service
A service that serves as an anchor point for our connector's (e.g. taleo-connector, ats-connector) 
and other services that interact with ATS systems. This service will expose operations to do CRUD 
operations on this type of data which will enable us to develop functionality such as selecting an ATS, 
changing one's ATS credentials or feature-set, updating status mappings, and more. 
It will also enable us to not rely on using AWS Param Store to store ClientTenant specific information as in our connectors.
