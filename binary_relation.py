import pandas as pd
import numpy as np

class BinaryRelation:
        
    def __init__(self, array, desired_shape):
        try:
            if len(array) < desired_shape[0] * desired_shape[1]:
                raise ValueError
                
            self.relation = array.reshape(desired_shape)
            
            self.n_rows = desired_shape[0]
            self.n_cols = desired_shape[1]
            
        except ValueError:
            print("Shape error. Desired shape {} doesn't match the length of the given array {}".format(desired_shape, len(array)))
        
    def printRelation(self, relation=None):
        if relation is not None:
            print(relation)
        else:
            print(self.relation)
        print()
    
    def isReflexive(self):
        is_reflexive = True
        
        for i in range(self.n_rows):
            if self.relation[i][i] != 1:
                is_reflexive = False
                break
                
            if not is_reflexive:
                break
        
        if is_reflexive:
            print('Binary relation is **Reflexive**')
        else:
            print('Binary relation is not **Reflexive**')
        
    
    def isIrreflexive(self):
        is_irreflexive = True
        
        for i in range(self.n_rows):
            if self.relation[i][i] != 0:
                is_irreflexive = False
                break
                
            if not is_irreflexive:
                break
        
        if is_irreflexive:
            print('Binary relation is **Irreflexive**')
        else:
            print('Binary relation is not **Irreflexive**')
    
    def isSymmetric(self):
        is_symmetric = True
        
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.relation[i][j] != self.relation[j][i]:
                    is_symmetric = False
                    break

                if not is_symmetric:
                    break

            if not is_symmetric:
                break

        if is_symmetric:
            print('Binary relation is **Symmetric**')
        else:
            print('Binary relation is not **Symmetric**')
    
    def isAntisymmetric(self):
        is_antisymmetric = True
        
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.relation[i][j] and self.relation[j][i] != 0:
                    is_antisymmetric = False
                    break

                if not is_antisymmetric:
                    break

            if not is_antisymmetric:
                break

        if is_antisymmetric:
            print('Binary relation is **Antisymmetric**')
        else:
            print('Binary relation is not **Antisymmetric**')
    
    def isAssymetric(self):
        is_assymmetric = True
        
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.relation[i][j] and self.relation[j][i] != 0 and i == j:
                    is_assymmetric = False
                    break

                if not is_assymmetric:
                    break

            if not is_assymmetric:
                break

        if is_assymmetric:
            print('Binary relation is **Assymmetric**')
        else:
            print('Binary relation is not **Assymmetric**')
    
    def isTransitive(self):
        is_transitive = True
        r2 = self.composition(self.relation)
#         self.printRelation(r2)
        
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if r2[i][j] != self.relation[i][j]:
                    is_transitive = False
                    break
                
                if not is_transitive:
                    break

            if not is_transitive:
                break
        
        if is_transitive:
            print('Binary relation is **Transitive**')
        else:
            print('Binary relation is not **Transitive**')
    
    def composition(self, new_relation):
        try:
            if self.n_cols != new_relation.shape[0]:
                raise ValueError
                
            compos_relation = self.relation.copy()
            min_elem_arr = np.zeros(self.n_rows)
        
            for i in range(self.n_rows):
                for j in range(self.n_cols):
                    for k in range(self.n_cols):
                        min_elem_arr[j] = min(self.relation[i][k], new_relation[k][j])            

                    compos_relation[i][j] = max(min_elem_arr)

            return compos_relation
    
        except ValueError:
            print("Shape error. Number of columns in input relation {} doesn't match number of rows in the given relation {}".format(self.n_cols, new_relation.shape[0]))
            return
        
    def strictRelation(self):
        inversed = self.inverseRelation()
        strict = np.subtract(self.relation, inversed)
        strict[strict < 0] = 0
#         self.printRelation(strict)
        return strict
    
    def inverseRelation(self):
        inversed = np.rot90(np.fliplr(self.relation.copy()))
#         self.printRelation(inversed)
        return inversed

    def complementRelation(self):
        complement = np.ones((self.n_rows, self.n_cols))
        complement = np.subtract(complement, self.relation)
        return complement

    def getMaximum(self):
        """
        Elements with all ones in a row of a binary relation
        """
        elems = []
        
        for i in range(self.n_rows):
            if np.all(self.relation[i] == 1):
                elems.append("x" + str(i+1))
        
        print("Maximum: {}".format(elems))
                
    def getMinimum(self):
        """
        Elements with all ones in a column of a binary relation
        """
        elems = []
        
        for i in range(self.n_rows):
            if np.all(self.relation.T[i] == 1):
                elems.append("x" + str(i+1))
        
        print("Minimum: {}".format(elems))

    
    def getMaximal(self):
        """
        Elements with all zeros in a column of a stricted relation
        """
        elems = []
        strict_relation = self.strictRelation()
        
        for i in range(self.n_rows):
            if np.all(strict_relation.T[i] == 0):
                elems.append("x" + str(i+1))
        
        print("Maximal elements: {}".format(elems))
    
    def getMinimal(self):
        """
        Elements with all zeros in a row of a stricted relation
        """
        elems = []
        strict_relation = self.strictRelation()
        
        for i in range(strict_relation.shape[0]):
            if np.all(strict_relation[i] == 0):
                elems.append("x" + str(i+1))
                
        print("Minimal elements: {}".format(elems))

if __name__ == '__main__':
    relation_array = np.array([1, 1, 0, 1, 0,
                               1, 1, 1, 1, 1,
                               1, 0, 0, 1, 1,
                               1, 1, 1, 1, 1,
                               0, 1, 0, 1, 0])
    relation_shape = (5, 5)
    
    relation = BinaryRelation(relation_array, relation_shape)

    print("Relation R:")
    relation.printRelation()
    relation.isReflexive()
    relation.isIrreflexive()
    relation.isSymmetric()
    relation.isAntisymmetric()
    relation.isAssymetric()
    relation.isTransitive()
    relation.strictRelation()
    relation.getMaximum()
    relation.getMinimum()
    relation.getMaximal()
    relation.getMinimal()
    print()
    
#     print("Relation R^2:")
#     r2 = relation.composition(relation.relation)
#     relation.printRelation(r2)
    
    print("Relation R^-1:")
    r_inv = relation.inverseRelation()
    relation.printRelation(r_inv)
    
#     print("Relation R^s:")
#     r_strict = relation.strictRelation()
#     relation.printRelation(r_strict)
    
    print("Relation ¬R:")
    r_comp = relation.complementRelation()
    relation.printRelation(r_comp)