class IPAddress:
    def __init__(self, ip):

        if isinstance(ip, (list, tuple)):
            for i, item in enumerate(ip):
                if item < 0 or item > 255: raise ValueError("Полный диапазон IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.")
            else: self._ip = ".".join(map(str, ip))
        else:
            for i, item in enumerate(map(int, str(ip).split("."))):
                if item < 0 or item > 255: raise ValueError("Полный диапазон IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.")
            else: self._ip = ip

    def __str__(self): return f"<{self._ip}>"
    def __repr__(self): return f"IPAddress('<{self._ip}>')"