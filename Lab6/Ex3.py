def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress


def test_determine_progress(determine_progress):
    """Test function that checks all possible return values of determine_progress1"""
    
    # Test case 1: "Get going!" when spins == 0
    assert determine_progress(0, 0) == "Get going!", "Should return 'Get going!' when spins is 0"
    
    # Test case 2: "Get going!" when hits == 0 (ratio is 0)
    assert determine_progress(0, 5) == "Get going!", "Should return 'Get going!' when hits is 0"
    
    # Test case 3: "On your way!" when 0 < ratio < 0.25
    assert determine_progress(1, 10) == "On your way!", "Should return 'On your way!' for ratio between 0 and 0.25"
    assert determine_progress(2, 10) == "On your way!", "Should return 'On your way!' for ratio 0.2"
    
    # Test case 4: "Almost there!" when 0.25 <= ratio < 0.5
    assert determine_progress(3, 10) == "Almost there!", "Should return 'Almost there!' for ratio 0.3"
    assert determine_progress(4, 10) == "Almost there!", "Should return 'Almost there!' for ratio 0.4 (< 0.5)"
    
    # Test case 5: "You win!" when ratio >= 0.5 and hits < spins
    assert determine_progress(5, 10) == "You win!", "Should return 'You win!' when ratio 0.5 and hits < spins"
    assert determine_progress(6, 10) == "You win!", "Should return 'You win!' for ratio 0.6"
    
    print("All tests passed!")

# Run the test
test_determine_progress(determine_progress1)