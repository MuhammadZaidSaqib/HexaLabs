# Name: Muhammad Zaid Saqib
# Reg No : B24F1722CYS084
# Section : CYS Green
# Date : 06/12/2025
# Open Ended Lab

#Q2

'''
Scenario: Sports Tournament Scheduling
A city-wide sports tournament involves multiple sports, teams, and venues.
Constraints:
1.	Each team plays only once per day, and matches cannot overlap for shared players or referees.
2.	Fields and courts have limited availability and some maintenance periods.
3.	High-priority matches should be in prime time slots.
4.	Some matches require specific equipment or indoor/outdoor venues.
5.	Teams from different regions may have travel constraints affecting availability.
6.	Matches for the same sport should be spread across venues to minimize congestion.
7.	Some final matches must follow a strict sequence after semifinals.
Goal:
Develop a tournament schedule that satisfies all constraints, minimizes conflicts, and ensures fair competition across teams and venues.

'''
# python
import random
from collections import defaultdict

class Team:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        self.availability = set()  # days available to play
        self.matches = []  # scheduled matches
    def __repr__(self):
        return self.name

class Venue:
    def __init__(self, name, sport_type):
        self.name = name
        self.sport_type = sport_type
        self.availability = set()  # days available for matches
    def __repr__(self):
        return self.name

class Match:
    def __init__(self, team1, team2, sport_type, priority=False, id=None):
        self.id = id or f"{team1.name}-{team2.name}"
        self.team1 = team1
        self.team2 = team2
        self.sport_type = sport_type
        self.priority = priority  # high-priority match (bool)
        self.scheduled_day = None
        self.venue = None
    def __repr__(self):
        return f"{self.team1} vs {self.team2} ({self.sport_type})"

class TournamentScheduler:
    def __init__(self, teams, venues, matches, days):
        self.teams = teams
        self.venues = venues
        self.matches = matches
        self.days = list(days)
        self.schedule = defaultdict(list)  # day -> list of matches
        # track booked venues per day to avoid double-booking a venue same day
        self.booked_venues = defaultdict(set)

    def is_conflict(self, match, day):
        # team already has a match that day?
        for scheduled_match in self.schedule[day]:
            if (match.team1 in (scheduled_match.team1, scheduled_match.team2) or
                match.team2 in (scheduled_match.team1, scheduled_match.team2)):
                return True
        return False

    def find_available_venues_for_day(self, match, day):
        # return list of venues that can host this sport and are available that day and not already booked
        candidates = []
        for venue in self.venues:
            if venue.sport_type != match.sport_type:
                continue
            if day not in venue.availability:
                continue
            if venue.name in self.booked_venues.get(day, set()):
                continue
            candidates.append(venue)
        return candidates

    def schedule_matches(self):
        # sort by priority first, then matches with fewer possible days (to reduce deadlocks)
        def possible_days_for_match(m):
            # days when both teams are available and at least one venue for sport is available
            team_days = m.team1.availability & m.team2.availability
            valid = []
            for d in team_days:
                if self.find_available_venues_for_day(m, d):
                    valid.append(d)
            return valid

        # precompute possible days to break ties
        match_options = []
        for m in self.matches:
            opts = possible_days_for_match(m)
            match_options.append((m, opts))

        # sort: priority desc, then ascending number of options (MRV)
        match_options.sort(key=lambda mo: (-int(mo[0].priority), len(mo[1]) if mo[1] else 999))

        for match, opts in match_options:
            if not opts:
                # no feasible day with current bookings/availabilities
                continue
            # pick the day among opts with minimal scheduled matches to spread across days
            chosen_day = min(opts, key=lambda d: (len(self.schedule[d]), d))
            # select a venue for that chosen day
            venues = self.find_available_venues_for_day(match, chosen_day)
            if not venues:
                # although opts indicated availability, another booking might have filled it; try other days
                placed = False
                for d in sorted(opts, key=lambda d: (len(self.schedule[d]), d)):
                    venues = self.find_available_venues_for_day(match, d)
                    if venues and not self.is_conflict(match, d):
                        chosen_day = d
                        placed = True
                        break
                if not placed:
                    continue
            # final conflict check (team/day)
            if self.is_conflict(match, chosen_day):
                # try alternative day
                placed = False
                for d in sorted(opts, key=lambda d: (len(self.schedule[d]), d)):
                    if self.is_conflict(match, d):
                        continue
                    venues = self.find_available_venues_for_day(match, d)
                    if venues:
                        chosen_day = d
                        placed = True
                        break
                if not placed:
                    continue
            # assign the first available venue for chosen_day
            chosen_venue = self.find_available_venues_for_day(match, chosen_day)[0]
            match.scheduled_day = chosen_day
            match.venue = chosen_venue
            self.schedule[chosen_day].append(match)
            self.booked_venues[chosen_day].add(chosen_venue.name)
            match.team1.matches.append(match)
            match.team2.matches.append(match)

    def print_schedule(self):
        # ensure all days are printed (even if empty)
        for day in sorted(self.days):
            print(f"Day {day}:")
            if not self.schedule.get(day):
                print("  No matches")
                continue
            for match in self.schedule[day]:
                print(f"  {match} at {match.venue}")

def generate_sample_data():
    teams = [Team(f"Team{i}", region=random.choice(['North', 'South', 'East', 'West'])) for i in range(8)]
    venues = [Venue(f"Venue{i}", sport_type=random.choice(['Soccer', 'Basketball', 'Tennis'])) for i in range(4)]
    days = list(range(1, 6))  # 5 days tournament
    for team in teams:
        team.availability = set(random.sample(days, k=random.randint(3, 5)))
    for venue in venues:
        venue.availability = set(random.sample(days, k=random.randint(3, 5)))
    matches = []
    for i in range(0, len(teams), 2):
        priority = (i // 2) < 2  # first two matches are high priority
        matches.append(Match(teams[i], teams[i+1],
                             sport_type=random.choice(['Soccer', 'Basketball', 'Tennis']),
                             priority=priority,
                             id=f"M{i//2+1}"))
    return teams, venues, matches, days

if __name__ == "__main__":
    teams, venues, matches, days = generate_sample_data()
    scheduler = TournamentScheduler(teams, venues, matches, days)
    scheduler.schedule_matches()
    scheduler.print_schedule()

#Description:
'''
This Python program simulates a scheduling system for a city-wide sports tournament by automatically assigning matches between 
teams to available days and venues while respecting real-world constraints such as team availability, venue availability, priority 
matches, and conflict avoidance. It defines separate classes for teams, venues, and matches to organize data effectively, where each 
team has specific available days, each venue supports only certain sports and has limited availability, and each match contains two teams,
a sport type, and a priority level. The TournamentScheduler class manages the scheduling process by first prioritizing high-importance matches 
and then selecting days that satisfy both teams’ availability and venue constraints. It ensures that no team plays more than one match per day 
and no venue is double-booked. The program also attempts to fairly distribute matches by choosing days with fewer scheduled games, reducing congestion
and improving balance. Sample data is randomly generated to mimic real tournament conditions, including regional teams, multi-sport venues, and varying 
availability. Finally, the completed schedule is printed day by day, showing which teams play, where they play, and on which day, effectively demonstrating
how automated scheduling can solve complex tournament management problems.
'''

