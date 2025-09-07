import torch

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Parameter(torch.rand([8, 16]))

    @torch.jit._overload_method()
    def forward(self, query: torch.Tensor) -> torch.Tensor: ...

    @torch.jit._overload_method()
    def forward(self, query: int):
        raise RuntimeError("Please provide actual arguments!")
 
    def forward(self, query): 
        return self.key @ query
