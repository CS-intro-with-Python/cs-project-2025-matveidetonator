"""
Seed script for Tarot cards database.
Rider-Waite Classic Deck (78 cards)
"""

# Major Arcana (22 cards)
MAJOR_ARCANA = [
    {
        'name': 'The Fool',
        'rank': '0',
        'meaning_upright': 'New beginnings, innocence, spontaneity, free spirit',
        'meaning_reversed': 'Recklessness, risk-taking, holding back, restlessness',
        'image_path': 'cards/00_the_fool.jpg'
    },
    {
        'name': 'The Magician',
        'rank': 'I',
        'meaning_upright': 'Willpower, manifestation, resourcefulness, skill',
        'meaning_reversed': 'Manipulation, poor planning, untapped talents, trickery',
        'image_path': 'cards/01_the_magician.jpg'
    },
    {
        'name': 'The High Priestess',
        'rank': 'II',
        'meaning_upright': 'Intuition, sacred knowledge, divine feminine, subconscious',
        'meaning_reversed': 'Secrets, withdrawal, silence, hidden agendas',
        'image_path': 'cards/02_the_high_priestess.jpg'
    },
    {
        'name': 'The Empress',
        'rank': 'III',
        'meaning_upright': 'Femininity, beauty, nature, nurturing, abundance',
        'meaning_reversed': 'Creative block, dependence, emptiness, smothering',
        'image_path': 'cards/03_the_empress.jpg'
    },
    {
        'name': 'The Emperor',
        'rank': 'IV',
        'meaning_upright': 'Authority, structure, control, fatherhood, stability',
        'meaning_reversed': 'Tyranny, rigidity, coldness, domination',
        'image_path': 'cards/04_the_emperor.jpg'
    },
    {
        'name': 'The Hierophant',
        'rank': 'V',
        'meaning_upright': 'Spiritual wisdom, tradition, conformity, morality',
        'meaning_reversed': 'Rebellion, subversiveness, new approaches, freedom',
        'image_path': 'cards/05_the_hierophant.jpg'
    },
    {
        'name': 'The Lovers',
        'rank': 'VI',
        'meaning_upright': 'Love, harmony, relationships, values alignment, choices',
        'meaning_reversed': 'Disharmony, imbalance, misalignment, bad choices',
        'image_path': 'cards/06_the_lovers.jpg'
    },
    {
        'name': 'The Chariot',
        'rank': 'VII',
        'meaning_upright': 'Control, willpower, success, determination, action',
        'meaning_reversed': 'Lack of control, opposition, lack of direction, aggression',
        'image_path': 'cards/07_the_chariot.jpg'
    },
    {
        'name': 'Strength',
        'rank': 'VIII',
        'meaning_upright': 'Courage, persuasion, influence, compassion, inner strength',
        'meaning_reversed': 'Self-doubt, weakness, insecurity, raw emotion',
        'image_path': 'cards/08_strength.jpg'
    },
    {
        'name': 'The Hermit',
        'rank': 'IX',
        'meaning_upright': 'Soul-searching, introspection, inner guidance, solitude',
        'meaning_reversed': 'Isolation, loneliness, withdrawal, lost',
        'image_path': 'cards/09_the_hermit.jpg'
    },
    {
        'name': 'Wheel of Fortune',
        'rank': 'X',
        'meaning_upright': 'Good luck, karma, life cycles, destiny, turning point',
        'meaning_reversed': 'Bad luck, resistance to change, breaking cycles',
        'image_path': 'cards/10_wheel_of_fortune.jpg'
    },
    {
        'name': 'Justice',
        'rank': 'XI',
        'meaning_upright': 'Justice, fairness, truth, cause and effect, law',
        'meaning_reversed': 'Unfairness, lack of accountability, dishonesty',
        'image_path': 'cards/11_justice.jpg'
    },
    {
        'name': 'The Hanged Man',
        'rank': 'XII',
        'meaning_upright': 'Pause, surrender, letting go, new perspectives',
        'meaning_reversed': 'Delays, resistance, stalling, indecision',
        'image_path': 'cards/12_the_hanged_man.jpg'
    },
    {
        'name': 'Death',
        'rank': 'XIII',
        'meaning_upright': 'Endings, change, transformation, transition, rebirth',
        'meaning_reversed': 'Resistance to change, personal transformation, inner purging',
        'image_path': 'cards/13_death.jpg'
    },
    {
        'name': 'Temperance',
        'rank': 'XIV',
        'meaning_upright': 'Balance, moderation, patience, purpose, meaning',
        'meaning_reversed': 'Imbalance, excess, self-healing, realignment',
        'image_path': 'cards/14_temperance.jpg'
    },
    {
        'name': 'The Devil',
        'rank': 'XV',
        'meaning_upright': 'Shadow self, attachment, addiction, restriction, sexuality',
        'meaning_reversed': 'Releasing limiting beliefs, exploring dark thoughts, detachment',
        'image_path': 'cards/15_the_devil.jpg'
    },
    {
        'name': 'The Tower',
        'rank': 'XVI',
        'meaning_upright': 'Sudden change, upheaval, chaos, revelation, awakening',
        'meaning_reversed': 'Personal transformation, fear of change, averting disaster',
        'image_path': 'cards/16_the_tower.jpg'
    },
    {
        'name': 'The Star',
        'rank': 'XVII',
        'meaning_upright': 'Hope, faith, purpose, renewal, spirituality, serenity',
        'meaning_reversed': 'Lack of faith, despair, self-trust, disconnection',
        'image_path': 'cards/17_the_star.jpg'
    },
    {
        'name': 'The Moon',
        'rank': 'XVIII',
        'meaning_upright': 'Illusion, fear, anxiety, subconscious, intuition',
        'meaning_reversed': 'Release of fear, repressed emotion, inner confusion',
        'image_path': 'cards/18_the_moon.jpg'
    },
    {
        'name': 'The Sun',
        'rank': 'XIX',
        'meaning_upright': 'Positivity, fun, warmth, success, vitality, joy',
        'meaning_reversed': 'Inner child, feeling down, overly optimistic',
        'image_path': 'cards/19_the_sun.jpg'
    },
    {
        'name': 'Judgement',
        'rank': 'XX',
        'meaning_upright': 'Judgement, rebirth, inner calling, absolution',
        'meaning_reversed': 'Self-doubt, inner critic, ignoring the call',
        'image_path': 'cards/20_judgement.jpg'
    },
    {
        'name': 'The World',
        'rank': 'XXI',
        'meaning_upright': 'Completion, integration, accomplishment, travel',
        'meaning_reversed': 'Seeking personal closure, short-cuts, delays',
        'image_path': 'cards/21_the_world.jpg'
    },
]

# Minor Arcana - Wands (14 cards)
WANDS = [
    {
        'name': 'Ace of Wands',
        'rank': 'Ace',
        'meaning_upright': 'Inspiration, new opportunities, growth, potential',
        'meaning_reversed': 'Delays, lack of motivation, weighed down',
        'image_path': 'cards/ace_of_wands.jpg'
    },
    {
        'name': 'Two of Wands',
        'rank': '2',
        'meaning_upright': 'Future planning, progress, decisions, discovery',
        'meaning_reversed': 'Fear of unknown, lack of planning, playing safe',
        'image_path': 'cards/02_of_wands.jpg'
    },
    {
        'name': 'Three of Wands',
        'rank': '3',
        'meaning_upright': 'Expansion, foresight, overseas opportunities',
        'meaning_reversed': 'Obstacles, delays, frustration, lack of foresight',
        'image_path': 'cards/03_of_wands.jpg'
    },
    {
        'name': 'Four of Wands',
        'rank': '4',
        'meaning_upright': 'Celebration, joy, harmony, relaxation, homecoming',
        'meaning_reversed': 'Personal celebration, inner harmony, conflict with others',
        'image_path': 'cards/04_of_wands.jpg'
    },
    {
        'name': 'Five of Wands',
        'rank': '5',
        'meaning_upright': 'Conflict, disagreements, competition, tension',
        'meaning_reversed': 'Inner conflict, conflict avoidance, release tension',
        'image_path': 'cards/05_of_wands.jpg'
    },
    {
        'name': 'Six of Wands',
        'rank': '6',
        'meaning_upright': 'Success, public recognition, progress, self-confidence',
        'meaning_reversed': 'Private achievement, personal definition of success, fall from grace',
        'image_path': 'cards/06_of_wands.jpg'
    },
    {
        'name': 'Seven of Wands',
        'rank': '7',
        'meaning_upright': 'Challenge, competition, protection, perseverance',
        'meaning_reversed': 'Exhaustion, giving up, overwhelmed',
        'image_path': 'cards/07_of_wands.jpg'
    },
    {
        'name': 'Eight of Wands',
        'rank': '8',
        'meaning_upright': 'Movement, fast paced change, action, alignment',
        'meaning_reversed': 'Delays, frustration, resisting change, internal alignment',
        'image_path': 'cards/08_of_wands.jpg'
    },
    {
        'name': 'Nine of Wands',
        'rank': '9',
        'meaning_upright': 'Resilience, courage, persistence, test of faith',
        'meaning_reversed': 'Inner resources, struggle, overwhelm, defensive',
        'image_path': 'cards/09_of_wands.jpg'
    },
    {
        'name': 'Ten of Wands',
        'rank': '10',
        'meaning_upright': 'Burden, extra responsibility, hard work, completion',
        'meaning_reversed': 'Doing it all, carrying the burden, delegation',
        'image_path': 'cards/10_of_wands.jpg'
    },
    {
        'name': 'Page of Wands',
        'rank': 'Page',
        'meaning_upright': 'Inspiration, ideas, discovery, limitless potential',
        'meaning_reversed': 'Newly formed ideas, redirect energy, self-limiting beliefs',
        'image_path': 'cards/page_of_wands.jpg'
    },
    {
        'name': 'Knight of Wands',
        'rank': 'Knight',
        'meaning_upright': 'Energy, passion, adventure, impulsiveness',
        'meaning_reversed': 'Haste, scattered energy, delays, frustration',
        'image_path': 'cards/knight_of_wands.jpg'
    },
    {
        'name': 'Queen of Wands',
        'rank': 'Queen',
        'meaning_upright': 'Courage, confidence, independence, social butterfly',
        'meaning_reversed': 'Self-respect, self-confidence, introverted, re-establish sense of self',
        'image_path': 'cards/queen_of_wands.jpg'
    },
    {
        'name': 'King of Wands',
        'rank': 'King',
        'meaning_upright': 'Natural leader, vision, entrepreneur, honour',
        'meaning_reversed': 'Impulsiveness, haste, ruthless, high expectations',
        'image_path': 'cards/king_of_wands.jpg'
    },
]

# Minor Arcana - Cups (14 cards)
CUPS = [
    {
        'name': 'Ace of Cups',
        'rank': 'Ace',
        'meaning_upright': 'Love, new relationships, compassion, creativity',
        'meaning_reversed': 'Self-love, intuition, repressed emotions',
        'image_path': 'cards/ace_of_cups.jpg'
    },
    {
        'name': 'Two of Cups',
        'rank': '2',
        'meaning_upright': 'Unified love, partnership, mutual attraction',
        'meaning_reversed': 'Self-love, break-ups, disharmony, distrust',
        'image_path': 'cards/02_of_cups.jpg'
    },
    {
        'name': 'Three of Cups',
        'rank': '3',
        'meaning_upright': 'Celebration, friendship, creativity, collaborations',
        'meaning_reversed': 'Independence, alone time, hardcore partying, gossip',
        'image_path': 'cards/03_of_cups.jpg'
    },
    {
        'name': 'Four of Cups',
        'rank': '4',
        'meaning_upright': 'Meditation, contemplation, apathy, reevaluation',
        'meaning_reversed': 'Retreat, withdrawal, checking in for alignment',
        'image_path': 'cards/04_of_cups.jpg'
    },
    {
        'name': 'Five of Cups',
        'rank': '5',
        'meaning_upright': 'Regret, failure, disappointment, pessimism',
        'meaning_reversed': 'Personal setbacks, self-forgiveness, moving on',
        'image_path': 'cards/05_of_cups.jpg'
    },
    {
        'name': 'Six of Cups',
        'rank': '6',
        'meaning_upright': 'Revisiting the past, childhood memories, innocence',
        'meaning_reversed': 'Living in the past, forgiveness, lacking playfulness',
        'image_path': 'cards/06_of_cups.jpg'
    },
    {
        'name': 'Seven of Cups',
        'rank': '7',
        'meaning_upright': 'Opportunities, choices, wishful thinking, illusion',
        'meaning_reversed': 'Alignment, personal values, overwhelmed by choices',
        'image_path': 'cards/07_of_cups.jpg'
    },
    {
        'name': 'Eight of Cups',
        'rank': '8',
        'meaning_upright': 'Disappointment, abandonment, withdrawal, escapism',
        'meaning_reversed': 'Trying one more time, indecision, aimless drifting',
        'image_path': 'cards/08_of_cups.jpg'
    },
    {
        'name': 'Nine of Cups',
        'rank': '9',
        'meaning_upright': 'Contentment, satisfaction, gratitude, wish come true',
        'meaning_reversed': 'Inner happiness, materialism, dissatisfaction',
        'image_path': 'cards/09_of_cups.jpg'
    },
    {
        'name': 'Ten of Cups',
        'rank': '10',
        'meaning_upright': 'Divine love, blissful relationships, harmony, alignment',
        'meaning_reversed': 'Disconnection, misaligned values, struggling relationships',
        'image_path': 'cards/10_of_cups.jpg'
    },
    {
        'name': 'Page of Cups',
        'rank': 'Page',
        'meaning_upright': 'Creative opportunities, intuitive messages, curiosity',
        'meaning_reversed': 'New ideas, doubting intuition, creative blocks',
        'image_path': 'cards/page_of_cups.jpg'
    },
    {
        'name': 'Knight of Cups',
        'rank': 'Knight',
        'meaning_upright': 'Creativity, romance, charm, imagination, beauty',
        'meaning_reversed': 'Overactive imagination, unrealistic, jealousy',
        'image_path': 'cards/knight_of_cups.jpg'
    },
    {
        'name': 'Queen of Cups',
        'rank': 'Queen',
        'meaning_upright': 'Compassionate, caring, emotionally stable, intuitive',
        'meaning_reversed': 'Inner feelings, self-care, self-love, co-dependency',
        'image_path': 'cards/queen_of_cups.jpg'
    },
    {
        'name': 'King of Cups',
        'rank': 'King',
        'meaning_upright': 'Emotionally balanced, compassionate, diplomatic',
        'meaning_reversed': 'Self-compassion, inner feelings, moodiness, emotionally manipulative',
        'image_path': 'cards/king_of_cups.jpg'
    },
]

# Minor Arcana - Swords (14 cards)
SWORDS = [
    {
        'name': 'Ace of Swords',
        'rank': 'Ace',
        'meaning_upright': 'Breakthroughs, new ideas, mental clarity, success',
        'meaning_reversed': 'Inner clarity, re-thinking an idea, clouded judgement',
        'image_path': 'cards/ace_of_swords.jpg'
    },
    {
        'name': 'Two of Swords',
        'rank': '2',
        'meaning_upright': 'Difficult decisions, weighing options, stalemate',
        'meaning_reversed': 'Indecision, confusion, information overload',
        'image_path': 'cards/02_of_swords.jpg'
    },
    {
        'name': 'Three of Swords',
        'rank': '3',
        'meaning_upright': 'Heartbreak, emotional pain, sorrow, grief',
        'meaning_reversed': 'Negative self-talk, releasing pain, optimism',
        'image_path': 'cards/03_of_swords.jpg'
    },
    {
        'name': 'Four of Swords',
        'rank': '4',
        'meaning_upright': 'Rest, relaxation, meditation, contemplation',
        'meaning_reversed': 'Exhaustion, burn-out, deep contemplation, stagnation',
        'image_path': 'cards/04_of_swords.jpg'
    },
    {
        'name': 'Five of Swords',
        'rank': '5',
        'meaning_upright': 'Conflict, disagreements, competition, defeat',
        'meaning_reversed': 'Reconciliation, making amends, past resentment',
        'image_path': 'cards/05_of_swords.jpg'
    },
    {
        'name': 'Six of Swords',
        'rank': '6',
        'meaning_upright': 'Transition, change, rite of passage, releasing baggage',
        'meaning_reversed': 'Personal transition, resistance to change, unfinished business',
        'image_path': 'cards/06_of_swords.jpg'
    },
    {
        'name': 'Seven of Swords',
        'rank': '7',
        'meaning_upright': 'Betrayal, deception, getting away with something',
        'meaning_reversed': 'Imposter syndrome, self-deceit, keeping secrets',
        'image_path': 'cards/07_of_swords.jpg'
    },
    {
        'name': 'Eight of Swords',
        'rank': '8',
        'meaning_upright': 'Negative thoughts, self-imposed restriction, imprisonment',
        'meaning_reversed': 'Self-limiting beliefs, inner critic, releasing negative thoughts',
        'image_path': 'cards/08_of_swords.jpg'
    },
    {
        'name': 'Nine of Swords',
        'rank': '9',
        'meaning_upright': 'Anxiety, worry, fear, depression, nightmares',
        'meaning_reversed': 'Inner turmoil, deep-seated fears, secrets, releasing worry',
        'image_path': 'cards/09_of_swords.jpg'
    },
    {
        'name': 'Ten of Swords',
        'rank': '10',
        'meaning_upright': 'Painful endings, deep wounds, betrayal, loss',
        'meaning_reversed': 'Recovery, regeneration, resisting an inevitable end',
        'image_path': 'cards/10_of_swords.jpg'
    },
    {
        'name': 'Page of Swords',
        'rank': 'Page',
        'meaning_upright': 'New ideas, curiosity, thirst for knowledge',
        'meaning_reversed': 'Self-expression, all talk and no action, haphazard',
        'image_path': 'cards/page_of_swords.jpg'
    },
    {
        'name': 'Knight of Swords',
        'rank': 'Knight',
        'meaning_upright': 'Ambitious, action-oriented, driven, fast thinking',
        'meaning_reversed': 'Restless, unfocused, impulsive, burn-out',
        'image_path': 'cards/knight_of_swords.jpg'
    },
    {
        'name': 'Queen of Swords',
        'rank': 'Queen',
        'meaning_upright': 'Independent, unbiased judgement, clear boundaries',
        'meaning_reversed': 'Overly emotional, easily influenced, cold-hearted',
        'image_path': 'cards/queen_of_swords.jpg'
    },
    {
        'name': 'King of Swords',
        'rank': 'King',
        'meaning_upright': 'Mental clarity, intellectual power, authority, truth',
        'meaning_reversed': 'Quiet power, inner truth, misuse of power, manipulation',
        'image_path': 'cards/king_of_swords.jpg'
    },
]

# Minor Arcana - Pentacles (14 cards)
PENTACLES = [
    {
        'name': 'Ace of Pentacles',
        'rank': 'Ace',
        'meaning_upright': 'New financial opportunity, manifestation, abundance',
        'meaning_reversed': 'Lost opportunity, lack of planning, scarcity mindset',
        'image_path': 'cards/ace_of_pentacles.jpg'
    },
    {
        'name': 'Two of Pentacles',
        'rank': '2',
        'meaning_upright': 'Multiple priorities, time management, adaptability',
        'meaning_reversed': 'Over-committed, disorganization, reprioritization',
        'image_path': 'cards/02_of_pentacles.jpg'
    },
    {
        'name': 'Three of Pentacles',
        'rank': '3',
        'meaning_upright': 'Teamwork, collaboration, learning, implementation',
        'meaning_reversed': 'Disharmony, misalignment, working alone',
        'image_path': 'cards/03_of_pentacles.jpg'
    },
    {
        'name': 'Four of Pentacles',
        'rank': '4',
        'meaning_upright': 'Saving money, security, conservatism, scarcity',
        'meaning_reversed': 'Over-spending, greed, self-protection',
        'image_path': 'cards/04_of_pentacles.jpg'
    },
    {
        'name': 'Five of Pentacles',
        'rank': '5',
        'meaning_upright': 'Financial loss, poverty, lack mindset, isolation',
        'meaning_reversed': 'Recovery from financial loss, spiritual poverty',
        'image_path': 'cards/05_of_pentacles.jpg'
    },
    {
        'name': 'Six of Pentacles',
        'rank': '6',
        'meaning_upright': 'Giving, receiving, sharing wealth, generosity',
        'meaning_reversed': 'Self-care, unpaid debts, one-sided charity',
        'image_path': 'cards/06_of_pentacles.jpg'
    },
    {
        'name': 'Seven of Pentacles',
        'rank': '7',
        'meaning_upright': 'Long-term view, sustainable results, perseverance',
        'meaning_reversed': 'Lack of long-term vision, limited success, impatience',
        'image_path': 'cards/07_of_pentacles.jpg'
    },
    {
        'name': 'Eight of Pentacles',
        'rank': '8',
        'meaning_upright': 'Apprenticeship, repetitive tasks, mastery, skill',
        'meaning_reversed': 'Self-development, perfectionism, misdirected activity',
        'image_path': 'cards/08_of_pentacles.jpg'
    },
    {
        'name': 'Nine of Pentacles',
        'rank': '9',
        'meaning_upright': 'Abundance, luxury, self-sufficiency, financial independence',
        'meaning_reversed': 'Self-worth, over-investment in work, hustling',
        'image_path': 'cards/09_of_pentacles.jpg'
    },
    {
        'name': 'Ten of Pentacles',
        'rank': '10',
        'meaning_upright': 'Wealth, financial security, family, long-term success',
        'meaning_reversed': 'Financial failure, loneliness, loss',
        'image_path': 'cards/10_of_pentacles.jpg'
    },
    {
        'name': 'Page of Pentacles',
        'rank': 'Page',
        'meaning_upright': 'Manifestation, financial opportunity, skill development',
        'meaning_reversed': 'Lack of progress, procrastination, learn from failure',
        'image_path': 'cards/page_of_pentacles.jpg'
    },
    {
        'name': 'Knight of Pentacles',
        'rank': 'Knight',
        'meaning_upright': 'Hard work, productivity, routine, conservatism',
        'meaning_reversed': 'Self-discipline, boredom, feeling stuck, perfectionism',
        'image_path': 'cards/knight_of_pentacles.jpg'
    },
    {
        'name': 'Queen of Pentacles',
        'rank': 'Queen',
        'meaning_upright': 'Nurturing, practical, providing financially, working parent',
        'meaning_reversed': 'Financial independence, self-care, work-home conflict',
        'image_path': 'cards/queen_of_pentacles.jpg'
    },
    {
        'name': 'King of Pentacles',
        'rank': 'King',
        'meaning_upright': 'Wealth, business, leadership, security, discipline',
        'meaning_reversed': 'Financially inept, obsessed with wealth, stubborn',
        'image_path': 'cards/king_of_pentacles.jpg'
    },
]


def get_all_cards():
    """Get all 78 tarot cards with their data."""
    cards = []
    
    # Major Arcana (no suit)
    for card in MAJOR_ARCANA:
        cards.append({
            'name': card['name'],
            'suit': None,
            'rank': card['rank'],
            'meaning_upright': card['meaning_upright'],
            'meaning_reversed': card['meaning_reversed'],
            'image_path': card['image_path']
        })
    
    # Minor Arcana
    suits = [
        ('Wands', WANDS),
        ('Cups', CUPS),
        ('Swords', SWORDS),
        ('Pentacles', PENTACLES)
    ]
    
    for suit_name, suit_cards in suits:
        for card in suit_cards:
            cards.append({
                'name': card['name'],
                'suit': suit_name,
                'rank': card['rank'],
                'meaning_upright': card['meaning_upright'],
                'meaning_reversed': card['meaning_reversed'],
                'image_path': card['image_path']
            })
    
    return cards


def seed_database(db, Card):
    """Seed the database with all tarot cards."""
    # Check if cards already exist
    if Card.query.count() > 0:
        print(f"Database already has {Card.query.count()} cards. Skipping seed.")
        return False
    
    cards = get_all_cards()
    for card_data in cards:
        card = Card(**card_data)
        db.session.add(card)
    
    db.session.commit()
    print(f"Successfully seeded {len(cards)} tarot cards!")
    return True


if __name__ == '__main__':
    # For testing - print all cards
    cards = get_all_cards()
    print(f"Total cards: {len(cards)}")
    for i, card in enumerate(cards, 1):
        print(f"{i}. {card['name']} ({card['suit'] or 'Major Arcana'})")
