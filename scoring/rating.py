def get_rating(score):
            if score >= 91:
                return "A+"
            elif score >= 81:
                return "A-"
            elif score >= 71:
                return "B+"
            elif score >= 61:
                return "B-"
            elif score >= 51:
                return "C+"
            elif score >= 41:
                return "C-"
            elif score >= 31:
                return "D"
            else:
                return "F"