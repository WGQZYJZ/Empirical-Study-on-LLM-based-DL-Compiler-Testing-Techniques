
class Model(torch.nn.Module):
    def __init__(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        super().__init__()
        self._scale = 1e-5
        self._softmax = torch.nn.Softmax(dim=-1)
 
    @staticmethod
    def scaled_dot_product(query: torch.Tensor, key: torch.Tensor, scale: float):
        qk = query @ key.transpose(-2, -1)
        return qk / scale
 
    @classmethod
    def drop(cls, x: torch.Tensor, p=0., inplace=False):
        return torch.nn.functional.dropout(x, p=p, inplace=inplace)
    
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor: 
        qk = self.scaled_dot_product(query, key, self._scale)
        output = self._softmax(qk).matmul(value)
        return output

m  = Model()

 # Inputs to the model 
 query  = torch.randn(16, 32)
 key   = torch.randn(16, 32)
 value = torch.randn(16, 32)
 
 # Call the function with the provided inputs and get an output for a reference check
 