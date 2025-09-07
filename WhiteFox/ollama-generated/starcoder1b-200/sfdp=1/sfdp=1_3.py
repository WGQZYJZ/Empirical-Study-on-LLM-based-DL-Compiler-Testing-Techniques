
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 10)
        self.key   = torch.nn.Linear(768, 25)
        self.value = torch.nn.Linear(768, 30)
 
    def forward(self, x):
        q  = self.query(x)  # Query tensor
        k  = self.key(x)    # Key tensor
        v  = self.value(x)  # Value tensor
 
        k_sq = torch.pow(k, 2)  # Compute squared difference between the input and key tensors
        dot = torch.matmul(q, k.transpose(-1, -2))  # Compute dot product of query and key tensors
 
        # Compute the inverse scale factor for the dot product
        inv_scale_factor = k_sq / (k_sq + v)  # Compute the inverse square root

        # Apply softmax on the scaled dot product
        softmax_qk = dot.softmax(dim=-1)  # Apply softmax to the scaled dot product
 
        # Dropout on the output of the softmax operation
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output

        # Compute the dot product between the dropout and value tensors
        output = dropout_qk.matmul(v)
 
        return output


# Initializing the model
m = Model()


