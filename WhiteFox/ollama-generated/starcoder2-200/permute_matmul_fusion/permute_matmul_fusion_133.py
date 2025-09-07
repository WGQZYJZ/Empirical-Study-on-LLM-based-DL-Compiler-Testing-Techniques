
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):

        # Case 1: t1 = input_tensorA.permute(...) and torch.bmm(t1, x2) is invoked.

        v3  = self.__helper__(x1, x2) # The model method __helper__ performs the permutation on one of the input tensors
        v4  = torch.bmm(v3, 0) # or  torch.matmul(v3, 0)

        return [
            v3, 
            v4
        ]

    def __helper__(self, x1, x2):
        
        # Case 2: t1 = input_tensorA.permute(...) and t2 = input_tensorB.permute(...), 
        # the model method __helper__ performs both permutations on its input tensors

        return torch.bmm(x1, x2)


# Initializing the model
m  = Model()
