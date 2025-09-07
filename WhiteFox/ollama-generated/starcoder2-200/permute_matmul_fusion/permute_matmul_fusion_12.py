
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = x1.permute([0,2,1])
        v2  = torch.bmm(v1[:, :, None], self.__output__)
        return v2


# Initializing the model and its weights