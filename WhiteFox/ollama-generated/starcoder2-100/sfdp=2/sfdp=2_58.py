
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.inv_scale = 0.5
        self.query = torch.nn.Parameter(
            torch.ones((2, 3), dtype=torch.float64) / (1 + np.random.normal())) 
        self.key = torch.nn.Parameter(
            torch.ones((3, 2), dtype=torch.float64)) 
        self.value = torch.nn.Parameter(
            torch.zeros((3, 4), dtype=torch.float64) + np.random.normal())
 
    def forward(self):
        qk = torch.matmul(self.query, self.key.transpose(-2, -1)) 
        scaled_qk = qk / inv_scale
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)   
        output  = dropout_qk.matmul(self.value) 
        return output


# Initializing the model
model = Model()
 
# Input to the model
query = torch.rand((2, 3))
key = torch.rand((3, 2))
value = torch.rand((3, 4))

