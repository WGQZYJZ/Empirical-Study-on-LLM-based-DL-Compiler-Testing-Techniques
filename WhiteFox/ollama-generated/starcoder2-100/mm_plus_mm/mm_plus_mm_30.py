
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1  = torch.mm(x1, y2) + torch.mm(y2, y2)
        return v1


# Initializing the model<|end_of_code|>
m  = Model()


