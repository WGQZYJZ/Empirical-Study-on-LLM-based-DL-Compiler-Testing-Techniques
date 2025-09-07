

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(128, 64))
 
    def forward(self, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        inv_scale_factor = 0.53997612

        scaled_qk = self.query @ (key / inv_scale_factor).transpose(-2, -1)

        dropout_output = torch.nn.functional.dropout(scaled_qk.softmax(dim=-1), p=0.438584535)
 
        output  =  dropout_output @ value
        return output


# Initializing the model
m  = Model()


# Inputs to the model
key, value = torch.randn(2, 3, 64), torch.randn(1, 78, 64)

