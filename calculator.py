# test_dependency.py
import nonexistent_module  # Will fail

def test():
    pass

if __name__ == "__main__":
    test()
