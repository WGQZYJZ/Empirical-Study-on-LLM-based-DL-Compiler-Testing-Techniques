
class Model(torch.nn.Module):
    def __init__(self, length1, length2, length3):
        super().__init__()
        self.mm = torch.nn.MM(length1)
 
    def forward(self, x1, x2):
        v1  = mm([x1])
        v2  = mm([x1], [x2])

        return [v1] + v2


# Initializing the model and providing the list length
mm = Model(3, 5)
print(mm.__output__)
