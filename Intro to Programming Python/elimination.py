import networkx as nx

class PlayoffElimination:
    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            lines = f.readlines()

        self.num_teams = int(lines[0])
        self.teams = []
        self.wins = []
        self.losses = []
        self.remaining = []
        self.schedule = []
        for i in range(1, self.num_teams+1):
            line = lines[i].strip().split()
            self.teams.append(line[0])
            self.wins.append(int(line[1]))
            self.losses.append(int(line[2]))
            self.remaining.append(int(line[3]))
            self.schedule.append(list(map(int, line[4:])))

    def create_flow_graph(self, team_index):
        # Create a flow graph with s, t, and one node for each team (excluding the given team).
        G = nx.DiGraph()
        G.add_node('s')
        G.add_node('t')
        for i in range(self.num_teams):
            if i != team_index:
                G.add_node(self.teams[i])

        # Add edges from s to each game between two other teams.
        for i in range(self.num_teams):
            if i != team_index:
                for j in range(i+1, self.num_teams):
                    if j != team_index:
                        G.add_node(f"{i}_{j}")
                        G.add_edge('s', f"{i}_{j}", capacity=self.schedule[i][j])

        # Add edges from each game to the teams that play in that game.
        for i in range(self.num_teams):
            if i != team_index:
                for j in range(i+1, self.num_teams):
                    if j != team_index:
                        G.add_edge(f"{i}_{j}", self.teams[i], capacity=float('inf'))
                        G.add_edge(f"{i}_{j}", self.teams[j], capacity=float('inf'))

        # Add edges from each team to t.
        for i in range(self.num_teams):
            if i != team_index:
                G.add_edge(self.teams[i], 't', capacity=self.wins[team_index] + self.remaining[team_index] - self.wins[i])

        return G

    def compute_max_flow(self, flow_graph):
        flow_value, flow_dict = nx.maximum_flow(flow_graph, 's', 't')
        return flow_value

    def is_trivially_eliminated(self, team_index):
        for i in range(self.num_teams):
            if i != team_index and self.wins[i] > self.wins[team_index] + self.remaining[team_index]:
                return self.int_to_team_name(i)
        return False

    def is_eliminated(self, team_index):
        # Check if the team is already trivially eliminated
        if self.is_trivially_eliminated(team_index):
            return True

        # Create a flow graph for the given team
        G = self.create_flow_graph(team_index)

        # Compute the max flow of the flow graph
        max_flow = self.compute_max_flow(G)

        # Check if the max flow saturates all the edges going out of the source node (s)
        total_capacity = 0
        for neighbor in G.neighbors('s'):
            total_capacity += G['s'][neighbor]['capacity']
        if max_flow == total_capacity:
            return False
        else:
            return True

    def int_to_team_name(self, team_index):
        return self.teams[team_index]

    def main(self):
        print(f" ")
        for i in range(self.num_teams):
            if self.is_trivially_eliminated(i):
                print(f"{self.int_to_team_name(i)} has been trivially eliminated by {self.is_trivially_eliminated(i)}.")
            elif self.is_eliminated(i):
                print(f"{self.int_to_team_name(i)} is eliminated.")
            else:
                print(f"{self.int_to_team_name(i)} is not eliminated.")

if __name__ == "__main__":

    playoff_elimination_1 = PlayoffElimination("potter.txt")
    playoff_elimination_1.main()
    playoff_elimination_2 = PlayoffElimination("mlb.txt")
    playoff_elimination_2.main()
    playoff_elimination_3 = PlayoffElimination("ivy_league.txt")
    playoff_elimination_3.main()
    playoff_elimination_4 = PlayoffElimination("world_cup.txt")
    playoff_elimination_4.main()