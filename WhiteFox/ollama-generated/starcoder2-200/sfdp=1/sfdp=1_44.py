
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn([128, 4096]))
        self.key = torch.nn.Parameter(torch.randn([128, 3754]))
 
    def forward(self, v1):
 
        qk = torch.matmul(v1, self.query) # Compute the dot product of the query and key tensors
        scaled_qk = qk / (0.9 + 0.65*qk.norm(dim=2).max(dim=-1)[-1]) # Scale the dot product by an inverse scale factor, which depends on the max norm value for each column in qk
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5834927655371094)  # Apply dropout to the softmax output with probability equal to 0.5834927655371094
        v2 = dropout_qk.matmul(self.key) # Compute the dot product of the dropout output and a value tensor
        return v2


# Initializing the model
m = Model()
# Inputs to the model
v1 = torch.randn([1, 3850])
