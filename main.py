import sys
sys.path.insert(0,"..")

from classes.individual import Individual

"""
create initial population
DO
    compute fitness
    select parents
    create offspring
    mutate offspring
WHILE population has not converged
end
"""

def main():
    person = Individual("John")
    print(person)

main()