
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, scale1=0.75):
        scaled_qk  = torch.matmul(query1, key1.transpose(-2, -1)).mul_(scale1)
        softmax_qk  = scaled_qk.softmax(dim=-1)
 
        output  = torch.nn.functional.dropout(
            softmax_qk, p=0.5).matmul(value1)
        return output

# Initializing the model
m  = Model()

# Inputs to the model