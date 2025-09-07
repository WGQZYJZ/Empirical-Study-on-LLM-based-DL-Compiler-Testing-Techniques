
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.key_layer = torch.nn.Linear(64, 1024)
        self.value_layer = torch.nn.Linear(1024, 512)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk.mul(scale_factor) 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()
query = torch.randn(8, 64, 256, 256).to(device)
key   = torch.randn(8, 1024, 3, 64).to(device)
value = torch.randn(8, 512, 7, 7).to(device)
 
# Input to the model
