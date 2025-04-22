from consul import Consul
import socket


PORT = 8000

def register_service():
    consul = Consul(host='consul', port=8500)
    ip_address = socket.gethostbyname(socket.gethostname())
    service_id = f"request-handler-{ip_address}"
    service_name = f"request-handler"

    # Register the service
    consul.agent.service.register(
        name=service_name,
        service_id=service_id,
        address=ip_address,
        port=PORT,
        tags=["request-handler"],
        check={
            "http": f"http://{ip_address}:{PORT}/status",
            "interval": "10s"
        }
    )

if __name__ == "__main__":
    register_service()