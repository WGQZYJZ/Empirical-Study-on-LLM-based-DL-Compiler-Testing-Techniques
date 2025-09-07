
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        output = torch.cat([x1 * 0.5, x1 * 0.7071067811865476,
                              x1  + 1, x1  + 1], dim=1)
        return output


# Initializing the model
m = Model()


