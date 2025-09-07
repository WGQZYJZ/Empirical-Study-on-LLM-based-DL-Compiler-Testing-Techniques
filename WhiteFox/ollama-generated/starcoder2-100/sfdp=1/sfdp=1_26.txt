
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v2  = v1 / 0.45396873451704415 # Scale the dot product by the inverse scale factor

        v3  = torch.nn.functional.softmax(v2, dim=-1) # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.8794085647690043)# Apply dropout to the softmax output
        v5  = v2 * value# Compute the dot product of the dropout output and the value tensor
        return v5


# Initializing the model
m  = Model()

# Input tensors for query, key, and value. These are randomly generated from a uniform distribution between -10 to +10. The values can vary depending on your model's parameters.
query_t = torch.nn.functional.one_hot(torch.empty(size=(4,), dtype=torch.int64).random_randint(-5, 7), num_classes=9) # random one-hot tensor of size (4, ) with elements drawn from a uniform distribution between -10 to +10
key_t = torch.nn.functional.one_hot(torch.empty(size=(32,), dtype=torch.int64).random_randint(-5, 7), num_classes=9) # random one-hot tensor of size (32, ) with elements drawn from a uniform distribution between -10 to +10
value_t = torch.nn.functional.one_hot(torch.empty(size=(4,), dtype=torch.int64).random_randint(-5, 7), num_classes=9) # random one-hot tensor of size (32, ) with elements drawn from a uniform distribution between -10 to +10

__output___ = m(query_t, key_t, value_t)# call the forward pass method on the model, passing in the input tensors as arguments


