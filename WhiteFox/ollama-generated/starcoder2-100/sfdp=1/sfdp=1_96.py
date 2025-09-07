
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor) -> torch.Tensor: 
        key  = <KEY>
        value  = <KEY>
        scaled_qk  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(scale_factor)
 
        softmax_qk  = torch.nn.functional.softmax(scaled_qk, dim=-1) 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
 
        return torch.matmul(dropout_qk, value),


# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn([1024*8])
key  = torch.randn([512*64])
value  = torch.randn([384*8])


