import random

# Mock Validators
validators = {
    "Alice": {"power": random.randint(10, 100), "stake": random.randint(10, 100)},
    "Bob": {"power": random.randint(10, 100), "stake": random.randint(10, 100)},
    "Charlie": {"power": random.randint(10, 100), "stake": random.randint(10, 100)}
}

# Proof of Work (PoW)
def simulate_pow():
    winner = max(validators, key=lambda x: validators[x]["power"])
    print("🔧 Consensus: Proof of Work (PoW)")
    print("Logic: Validator with highest computational power wins.")
    for name, v in validators.items():
        print(f"{name} -> Power: {v['power']}")
    print(f"Selected Validator: {winner}\n")

#  Proof of Stake (PoS)
def simulate_pos():
    winner = max(validators, key=lambda x: validators[x]["stake"])
    print(" Consensus: Proof of Stake (PoS)")
    print("Logic: Validator with highest stake wins.")
    for name, v in validators.items():
        print(f"{name} -> Stake: {v['stake']}")
    print(f"Selected Validator: {winner}\n")

# Delegated Proof of Stake (DPoS)
def simulate_dpos():
    delegates = ["Alice", "Bob", "Charlie"]
    voters = {
        "Voter1": random.choice(delegates),
        "Voter2": random.choice(delegates),
        "Voter3": random.choice(delegates)
    }

    vote_counts = {name: 0 for name in delegates}
    for vote in voters.values():
        vote_counts[vote] += 1

    winner = max(vote_counts, key=vote_counts.get)
    
    print(" Consensus: Delegated Proof of Stake (DPoS)")
    print("Logic: Voters elect a delegate with the highest votes.")
    print("Votes:")
    for voter, vote in voters.items():
        print(f"{voter} -> Voted for: {vote}")
    print("Vote Tally:")
    for name, count in vote_counts.items():
        print(f"{name} -> {count} vote(s)")
    print(f"Selected Validator (Delegate): {winner}\n")

# Run all simulations
simulate_pow()
simulate_pos()
simulate_dpos()
