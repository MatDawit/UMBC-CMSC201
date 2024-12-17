"""
File:    the_internet.py
Author:  Mathew Dawit
Date:    11/23/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
  A simple data structure to replicate some terminal commands.
"""


QUIT = "quit"
CREATE_SERVER = "create-server"
CREATE_CONNECTION = "create-connection"
SET_SERVER = "set-server"
TRACEROUTE = "traceroute"
TRACERT = "tracert"
PING = "ping"
IP_CONFIG = "ip-config"
DISPLAY_SERVERS = "display-servers"
HELP = "help"


def help():
    """
    Prints the available command options and their usage.
    """
    print("Command Options:")
    print(f"{CREATE_SERVER} <domain_name> <ipv4>")
    print(f"{CREATE_CONNECTION} <domain_name> <domain_name> <connection_time>")
    print(f"{SET_SERVER} <domain_name> or <ipv4>)")
    print(f"{TRACEROUTE}/{TRACERT} <domain name> or <ipv4>")
    print(f"{PING} <domain_name> or <ipv4>")
    print(f"{IP_CONFIG} server must be set")
    print(f"{DISPLAY_SERVERS} displays all servers and connections")
    print(f"{HELP} displays this screen")


def user_input(servers, main_server):
    """
    Processes user input and performs corresponding operations.
    :param servers: dict, the data structure containing server information.
    :param main_server: str, the currently active server.
    :return: tuple, a boolean indicating whether to quit and the updated main_server.
    """
    code_word = input(">>> ").lower().strip().split()

    # Handle empty input
    if not code_word:
        return False, main_server

    # Quit command
    if code_word[0] == QUIT:
        if len(code_word) != 1:
            print("Invalid Parameters")
            return False, main_server

        return True, main_server

    # Handle other commands based on input
    if code_word[0] == CREATE_SERVER:
        if len(code_word) != 3:
            print("Invalid Parameters")
            return False, main_server
        
        ip = code_word[2]
        server = code_word[1]
        validation = ip_check(ip, servers)

        if validation == "Valid":
            create_server(servers, server, ip)
        else:
            print(validation)

    elif code_word[0] == CREATE_CONNECTION:
        if len(code_word) != 4:
            print("Invalid Parameters")
            return False, main_server
        
        server_one = code_word[1]
        server_two = code_word[2]
        time = int(code_word[3])
        validation = connection_check(servers, server_one, server_two)

        if validation == "Valid":
            create_connection(servers, server_one, server_two, time)
        else:
            print(validation)

    elif code_word[0] == SET_SERVER:
        if len(code_word) != 2:
            print("Invalid Parameters")
            return False, main_server
        
        server = code_word[1]
        validation = server_check(servers, server)

        if validation == "Valid":
            main_server = set_server(server)
        else:
            print(validation)

    elif code_word[0] == TRACEROUTE or code_word[0] == TRACERT:
        if len(code_word) != 2:
            print("Invalid Parameters")
            return False, main_server
        
        address = code_word[1]
        validation = traceroute_and_ping_check(servers, address, main_server)

        if validation == "Valid":
            traceroute(servers, address, main_server)
        else:
            print(validation)

    elif code_word[0] == PING and len(code_word) == 2:
        address = code_word[1]
        validation = traceroute_and_ping_check(servers, address, main_server)
        
        if validation == "Valid":
            ping(servers, address, main_server)
        else:
            print(validation)

    elif code_word[0] == IP_CONFIG:
        if len(code_word) != 1:
            print("Invalid Parameters")
            return False, main_server
        
        validation = ip_config_check(main_server)

        if validation == "Valid":
            ip_config(servers, main_server)
        else:
            print(validation)

    elif code_word[0] == DISPLAY_SERVERS:
        if len(code_word) != 1:
            print("Invalid Parameters")
            return False, main_server
        
        validation = display_servers_check(servers)

        if validation == "Valid":
            display_servers(servers)
        else:
            print(validation)

    elif code_word[0] == HELP:
        if len(code_word) != 1:
            print("Invalid Parameters")
            return False, main_server
        
        help()

    elif not code_word:
        pass

    else:
        print(f"Invalid Command: {' '.join(code_word)}")


    return False, main_server


def ip_check(ip, servers):
    """
    Validates the given IP address.
    :param ip: str, the IP address to validate.
    :param servers: dict, the data structure containing server information.
    :return: str, a validation message.
    """
    ip_split = ip.strip().split('.')

    if len(ip_split) > 4:
        return "Invalid IP: Too many Periods"
    # Check if all parts of the IP are in valid range
    for numbers in ip_split:
        if not numbers:
            return "Invalid IP: Portion of Numbers greater than 255 or less than 0"
        if not (0 <= int(numbers) <= 255):
            return "Invalid IP: Portion of Numbers greater than 255 or less than 0"

    # Ensure IP is not already used
    for keys in servers.keys():
        if servers[keys]["ip_address"] == ip:
            return "Invalid IP: IP was used before"
            
    return "Valid"


def create_server(servers, server, ip):
    """
    Adds a new server to the network or updates the IP address of an existing server.
    :param servers: dict - The dictionary of all servers in the network.
    :param server: str - The name of the server.
    :param ip: str - The IPv4 address of the server.
    :return: None
    """
    if server not in servers.keys():
        # Create a new server entry
        servers[server] = {
            "ip_address": ip,
            "connection": [],
            "time": []
        }
    else:
        # Update the IP address of an existing server
        servers[server]["ip_address"] = ip

    print(f"Success: A server with name {server} was created at IP {ip}")


def connection_check(servers, server_one, server_two):
    """
    Checks whether a connection between two servers is valid or not.
    :param servers: dict - The dictionary of all servers in the network.
    :param server_one: str - Name of the first server.
    :param server_two: str - Name of the second server.
    :return: str - "Valid" if the connection can be created, otherwise an error message.
    """
    server_one_flag = False
    server_two_flag = False

    # Check if both servers exist
    for server in servers.keys():
        if server_one == server:
            server_one_flag = True
        elif server_two == server:
            server_two_flag = True

    if not server_one_flag or not server_two_flag:
        return "Invalid Connection: One of the servers does not exist"

    # Check if a connection already exists
    if server_one in servers[server_two]["connection"]:
        server_one_flag = False
    if server_two in servers[server_one]["connection"]:
        server_two_flag = False

    if not server_one_flag or not server_two_flag:
        return "Invalid Connection: Connection already exists"

    return "Valid"


def create_connection(servers, server_one, server_two, time):
    """
    Establishes a connection between two servers and assigns a connection time.
    :param servers: dict - The dictionary of all servers in the network.
    :param server_one: str - Name of the first server.
    :param server_two: str - Name of the second server.
    :param time: int - Connection time between the servers.
    :return: None
    """
    # Add mutual connections and time
    servers[server_one]["connection"].append(server_two)
    servers[server_one]["time"].append(time)
    servers[server_two]["connection"].append(server_one)
    servers[server_two]["time"].append(time)
    print(f"Success: A server with name {server_one} is now connected to {server_two}")


def server_check(servers, server):
    """
    Validates whether the server exists in the network.
    :param servers: dict - The dictionary of all servers in the network.
    :param server: str - The name of the server to validate.
    :return: str - "Valid" if the server exists, otherwise an error message.
    """
    if server in servers.keys():
        return "Valid"
    return "Invalid Server Setting: Server does not exist"


def set_server(server):
    """
    Sets the active server for subsequent operations.
    :param server: str - The name of the server to set.
    :return: str - The name of the active server.
    """
    print(f"Server {server} selected.")
    return server


def traceroute_and_ping_check(servers, address, set_server):
    """
    Validates whether the address is reachable and if the starting server is set.
    :param servers: dict - The dictionary of all servers in the network.
    :param address: str - The target server name or IP address.
    :param set_server: str - The starting server name.
    :return: str - "Valid" if checks pass, otherwise an error message.
    """
    address_flag = False

    if set_server == "":
        return "Starting Server not Set"

    # Check if the address is a valid server or IP address
    for server in servers.keys():
        if address == server:
            address_flag = True
        elif address == servers[server]["ip_address"]:
            address_flag = True
        
    if not address_flag:
        return "Invalid Input: Domain or IP not found"

    return "Valid"


def traceroute(servers, address, start_server):
    """
    Performs a traceroute from the start server to the destination address.
    :param servers: dict - The dictionary of all servers in the network.
    :param address: str - The destination server name or IP address.
    :param start_server: str - The starting server name.
    :return: None
    """
    visited = {}

    # Initialize visited dictionary and identify the destination server
    for server in servers:
        visited[server] = False
        if address == server:
            end_server = address
        elif address == servers[server]["ip_address"]:
            end_server = server

    route = traceroute_and_ping_rec(servers, start_server, end_server, visited)

    if route:
        print(f"Tracing route to {end_server} [{address}]")
        for i in range(len(route)):
            index = 0
            if i != 0:
                for y in range(len(servers[route[i]]["connection"])):
                    if servers[route[i]]["connection"][y] == route[i - 1]:
                        index = y

            if i == 0:
                print(f"\t{i}\t0\t[{servers[route[i]]['ip_address']}]\t{route[i]}")
            else:
                print(f"\t{i}\t{servers[route[i]]['time'][index]}\t[{servers[route[i]]['ip_address']}]\t{route[i]}")

        print("Trace complete.")
    else:
        print(f"Unable to route to target system name {address}")


def traceroute_and_ping_rec(servers, start_server, end_server, visited):
    """
    Recursive function to determine the path from the start server to the end server.
    :param servers: dict - The dictionary of all servers in the network.
    :param start_server: str - The starting server name.
    :param end_server: str - The destination server name.
    :param visited: dict - Dictionary to track visited servers.
    :return: list - The path from start_server to end_server if it exists.
    """
    path = []
    if start_server == end_server:
        return [end_server]

    visited[start_server] = True

    for next_place in servers[start_server]["connection"]:
        if not visited[next_place]:
            path = traceroute_and_ping_rec(servers, next_place, end_server, visited)
            if path:
                return [start_server] + path

    visited[start_server] = False
    return path


def ping(servers, address, start_server):
    """
    Simulates a ping operation from the start server to the destination address.
    :param servers: dict - The dictionary of all servers in the network.
    :param address: str - The destination server name or IP address.
    :param start_server: str - The starting server name.
    :return: None
    """
    visited = {}

    # Initialize visited dictionary and identify the destination server
    for server in servers:
        visited[server] = False
        if address == server:
            end_server = address
        elif address == servers[server]["ip_address"]:
            end_server = server

    route = traceroute_and_ping_rec(servers, start_server, end_server, visited)

    if route:
        time = 0
        for i in range(len(route)):
            if i != 0:
                for y in range(len(servers[route[i]]["connection"])):
                    if servers[route[i]]["connection"][y] == route[i - 1]:
                        time += servers[route[i]]["time"][y]

        print(f"Reply from {servers[end_server]['ip_address']} time = {time} ms")
    else:
        print(f"Unable to route to target system name {address}")


def ip_config_check(server):
    """
    Checks if a server is set for IP configuration.
    :param server: str - The name of the active server.
    :return: str - "Valid" if a server is set, otherwise an error message.
    """
    if server == "":
        return "Invalid Server Setting: Server is not set"
    return "Valid"


def ip_config(servers, server):
    """
    Displays the IP configuration of a specific server.
    :param servers: dict - The dictionary of all servers in the network.
    :param server: str - The name of the server to display configuration for.
    :return: None
    """
    print(f"{server}\t{servers[server]['ip_address']}")


def display_servers_check(servers):
    """
    Checks if there are servers available to display.
    :param servers: dict - The dictionary of all servers in the network.
    :return: str - "Valid" if there are servers to display, otherwise an error message.
    """
    if not servers:
        return "No Servers to Display"
    return "Valid"


def display_servers(servers):
    """
    Displays all servers in the network and their connections.
    :param servers: dict - The dictionary of all servers in the network.
    :return: None
    """
    for server in servers.keys():
        print(f"\t{server}\t{servers[server]['ip_address']}")
        for i in range(len(servers[server]["connection"])):
            print(f"\t\t{servers[server]['connection'][i]}\t{servers[servers[server]['connection'][i]]['ip_address']}\t{servers[server]['time'][i]}")


def internet_creation():
    """
    Initializes the network creation process, allowing user interaction for adding servers and connections.
    :return: None
    """
    internet = {}
    main_server = ""
    input_check, main_server = user_input(internet, main_server)

    while not input_check:
        input_check, main_server = user_input(internet, main_server)


if __name__ == '__main__':
  internet_creation()
