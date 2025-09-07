
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(20, 3)
        self.key   = torch.randn(20, 48) 
        self.value = torch.randn(20, 16*5)
        self.dropout_p = 0.7
 
        scale_factor = (self.query**2).mean().sqrt() + 1e-5

        self.softmax  = torch.nn.Softmax(dim=-1)
        self.inv_scale_factor  = 1/scale_factor
 
    def forward(self, input):
        qk  = torch.matmul(self.query, self.key.transpose(-2, -1)) 
        scaled_qk  = qk.div_(self.inv_scale_factor) # Scaled dot product
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output    = dropout_qk.matmul(self.value)

        return output

# Initializing the model
m  = Model()
 
# Input to the model
input = torch.randn(20, 16*5)

 # Output of the model
