import torch
from torch._C import randlike


class Model(torch.nn.Module):
    def __init__(self, a=None):
        super().__init__()
        self.a = a

    @torch.jit._overload_method()  # type: ignore[attr-defined]
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...
    
    def forward(self, x1):
        v1 = randlike(x1, int(x1.nelement() * self.a))

        return v1
$ python example_script.py 
Generating input_tensor
Initializing model, 
