
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return self._my_attention(x1)

    @torch.no_grad()  # Prevent dropout from being enabled in inference mode
    def _my_attention(self, x):
        query = torch.randn(32, 64, 512)
        key = torch.randn(32, 64, 512)
        value = torch.randn(32, 64, 512)
 
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk / math.sqrt(512) # Scale the dot product by a constant of sqrt(scale_factor). The scale factor was arbitrarily chosen to be 512
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)

        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.387)
 
        output = torch.matmul(dropout_qk, value) 
        return output


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(2, 3, 512)
__output__  = m(x1)