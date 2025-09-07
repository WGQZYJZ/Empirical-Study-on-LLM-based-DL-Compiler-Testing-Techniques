
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:

        # The scaling factor can be a constant or variable depending on the model being implemented.
        scale_factor  = 10.0
        
        scaled_query  = query / scale_factor 
        scaled_key = key / scale_factor
        qk  = torch.matmul(scaled_query, scaled_key.transpose(-2,-1))

        inv_scale_factor = 1./scale_factor

        # Compute the dot product of a scaled query and a scaled key.
        scaled_qk = qk.div(inv_scale_factor) 

        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.3, training=True)

        output = dropout_qk.matmul(value)
        return output
        
# Initializing the model
attnm  = AttentionModel()

 # Inputs to the model
input1  = torch.randn(256, 48, 7, 9)
input2  = torch.randn(256, 48, 7, 9)
input3  = torch.randn(256, 48, 7, 9)

__output__  = attnm(input1, input2, input3)
