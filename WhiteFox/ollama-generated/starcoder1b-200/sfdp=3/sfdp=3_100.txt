
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(1024, 512)
        self.k = torch.nn.Linear(512, 512)
        self.v = torch.nn.Linear(512, 512)
        self.dropout_p = dropout_p
 
    def forward(self, x):
        q = self.q(x)  # Apply pointwise linear operation to the input and return the output of the linear layer
        k = self.k(x)  # Apply pointwise linear operation to the input and return the output of the linear layer
        v = self.v(x)  # Apply pointwise linear operation to the input and return the output of the linear layer
 
        q = torch.nn.functional.dropout(q, p=self.dropout_p)  # Apply dropout to the output of the pointwise linear operation

        k = torch.nn.functional.dropout(k, p=self.dropout_p)  # Apply dropout to the output of the pointwise linear operation
 
        scaled_qk = q.matmul(k)
        scaled_qk = scaled_qk.mul(1 / math.sqrt(scaled_qk.size(-1)))
        softmax_qk = scaled_qk.softmax(-1)

        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
 
        return output


# Initializing the model
m = Model()


