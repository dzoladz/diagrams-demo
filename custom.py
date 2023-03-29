from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.network import Nginx
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.client import Users
from diagrams.onprem.logging import Graylog
from diagrams.aws.blockchain import QLDB
from diagrams.saas.chat import Slack
from diagrams.programming.framework import Starlette

graph_attributes = {
    "fontsize": "45",
    "bgcolor": "lightgrey",  # transparent
}

with Diagram(
    "Custom Nonsense using Custom Icons",
    outformat="png",
    filename="custom_diagram",
    direction="RL",
    graph_attr=graph_attributes,
    show=False
):

    ingress = Nginx("ingress")

    with Cluster("App", direction="LR"):
        uvicorn = Custom("Uvicorn", 'icons/uvicorn.png')
        fastapi = Custom("FastAPI", 'icons/fastapi.png')

    with Cluster("Service Cluster"):
        server_group = [
            Server("WIMPY"),
            Server("SuperMega"),
        ]

    with Cluster("Database Cluster"):
        primary = PostgreSQL("users")
        primary - PostgreSQL("replica") << server_group
        ingress >> primary

    users = Users()
    graylog = Graylog()
    blockchain = QLDB()
    slack = Slack()
    starlette = Starlette()

    ingress \
        >> Edge(color="darkgreen") \
        << fastapi

    users >> ingress
    starlette >> fastapi
    graylog >> fastapi
    graylog >> uvicorn
    graylog >> graylog
    blockchain - users
    slack >> primary

