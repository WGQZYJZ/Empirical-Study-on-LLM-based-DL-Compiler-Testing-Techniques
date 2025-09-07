
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        torch.full([x1.shape[0], 32768-1], 1, dtype=torch.int64)

	torch.cumsum(torch.full([args[0], args[1]], 1), dim = 1).tolist()



# Initializing the model