
class Model(torch.nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.query_linear = torch.nn.Linear(hidden_dim, hidden_dim)
        self.key_linear = torch.nn.Linear(hidden_dim, hidden_dim)
        self.value_linear = torch.nn.Linear(hidden_dim, hidden_dim)
 
    def forward(self, x1):
        q1 = self.query_linear(x1)
        k1 = self.key_linear(x1)
        v1 = self.value_linear(x1)
 
        scaled_qk  = q1.div(inv_scale_factor).softmax(dim=-1) # apply softmax to the dot product of query and key tensors 
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, v1).squeeze(dim=-2) # compute the dot product of the dropout output and the value tensor
 
        return output


# Initializing the model
m = Model()

