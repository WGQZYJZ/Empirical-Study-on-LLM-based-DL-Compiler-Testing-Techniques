
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1[0], x1[1]], dim=3) # 3rd dimension is concatenated with 4th dimension.
        v2 = v1.view(-1, v1.size()[3], v1.size()[4]) 
        v3 = torch.relu(v2)  

        return (v1, v2, v3)


# Initializing the model