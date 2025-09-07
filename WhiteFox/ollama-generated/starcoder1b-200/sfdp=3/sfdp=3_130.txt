
class Model(torch.nn.Module):
    def __init__(self, d_k):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_k)
        self.key    = torch.nn.Linear(d_model, d_k)
        self.value  = torch.nn.Parameter(torch.zeros((1, d_model)))
 
    def forward(self, x):
        query  = self.query(x).contiguous()
        key    = self.key(x).contiguous()
        value  = self.value.repeat_interleave(key.size(0), dim=0)  # Repeat the value tensor on all batches of keys
        qk     = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(self.scale_factor).contiguous()  # Scale the dot product by a factor
        dropout_qk = torch.nn.functional.dropout(scaled_qk.softmax(dim=-1), p=self.dropout_p)  # Apply dropout to the softmax output
        return self.value.repeat_interleave(key.size(0), dim=0).contiguous().matmul(dropout_qk.contiguous())


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
