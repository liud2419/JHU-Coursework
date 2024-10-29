def read_telemetry(file_name):
    """
    Reads and parses the telemetry data from a file.

    Parameters:
    file_name (str): The name of the file to read.

    Returns:
    list: A list of dictionaries containing the satellite telemetry data.
    Each dictionary contains the following keys:
        'country' (str): The country of ownership.
        'altitude' (float): The satellite's altitude (km).
        'velocity' (float): The satellite's velocity (km/s).
    """
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        satellites = []
        for i in range(n):
            data = file.readline().strip().split(',')
            country, altitude, velocity = data
            satellites.append({'country': country.strip(), 'altitude': float(altitude), 'velocity': float(velocity)})
    return satellites


def check_collisions(telemetry):
    """
    Checks for satellite collisions in the given telemetry data.

    Parameters:
    telemetry (list): A list of dictionaries containing the satellite telemetry data.
    Each dictionary contains the following keys:
        'country' (str): The country of ownership.
        'altitude' (float): The satellite's altitude (km).
        'velocity' (float): The satellite's velocity (km/s).

    Returns:
    dict: A dictionary mapping satellites at risk of collision to a list of other satellites they are at risk of colliding with.
    """
    collisions = {}
    for i, satellite1 in enumerate(telemetry):
        for j, satellite2 in enumerate(telemetry):
            if i != j:
                if satellite1['altitude'] == satellite2['altitude']:  # Same altitude
                    if satellite1['velocity'] * satellite2['velocity'] < 0:  # Opposite directions
                        if satellite1['country'] not in collisions:
                            collisions[satellite1['country']] = [satellite2['country']]
                        else:
                            collisions[satellite1['country']].append(satellite2['country'])
                    elif satellite1['velocity'] != satellite2['velocity']:  # Same direction, different velocities
                        if satellite1['country'] not in collisions:
                            collisions[satellite1['country']] = [satellite2['country']]
                        else:
                            collisions[satellite1['country']].append(satellite2['country'])
    return collisions


def main():
    file_names = ['satellites1-1.txt', 'satellites2-1.txt']
    for file_name in file_names:
        print("##### Space Command Simulation {} #####".format(file_names.index(file_name) + 1))
        telemetry = read_telemetry(file_name)
        collisions = check_collisions(telemetry)
        output_filename = file_name.replace('.txt', '_alerts.txt')
        with open(output_filename, 'w') as output_file:
            output_file.write("##### Space Command Simulation {} #####\n".format(file_names.index(file_name) + 1))
            for satellite in telemetry:
                country = satellite['country']
                if country not in collisions:
                    output_file.write("{} is not at risk for a collision.\n".format(country))
                    print("{} is not at risk for a collision.".format(country))
                else:
                    colliding_countries = collisions[country]
                    output_file.write("{} is at risk of colliding with {}.\n".format(country, colliding_countries))
                    print("{} is at risk of colliding with {}.".format(country, colliding_countries))
        print("")


if __name__ == "__main__":
    main()
