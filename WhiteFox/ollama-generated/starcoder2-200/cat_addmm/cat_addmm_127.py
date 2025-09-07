
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.addmm(x1, mat1, mat2) 
        return self._cat(v2, 3)

    @staticmethod
    def _cat(input: torch.Tensor, dim=0):
         v1  = torch.nn.functional.pad(
            input, (0, 4))
         return torch.cat([v1], dim=dim)

# Initializing the model