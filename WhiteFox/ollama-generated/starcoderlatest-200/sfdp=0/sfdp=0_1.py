
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # Initialize a query vector with shape (1, 512) and an output dimension of 1024
        self.query = torch.nn.Parameter(torch.randn(1, 1024))
 
        # Initialize a key vector with shape (512, 1024) and an output dimension of 1024
        self.key = torch.nn.Parameter(torch.randn(1024, 1024))
 
        # Initialize a value vector with shape (1024, 512) and an output dimension of 1024
        self.value = torch.nn.Parameter(torch.randn(1024, 1024))
 
    def forward(self, input):
        # Shape of query tensor: (batch_size, 768)
        # Shape of key tensor: (batch_size, 768)
        # Shape of value tensor: (batch_size, 768)
        q = self.query.repeat(input.shape[0], 1).permute([0,2,1])
 
        # Compute the attention weights with shape (batch_size, 768, 1024) and dtype float32
        attention_weights = torch.bmm(q, self.key) / math.sqrt(float(self.key.shape[-1]))
 
        # Apply softmax to each dimension of the output with shape (batch_size, 768, 1024) and dtype float32
        attention_weights = F.softmax(attention_weights, dim=-1)
 
        # Compute the weighted sum of the value tensor with shape (batch_size, 768, 512) and dtype float32
        output = torch.bmm(attention_weights, self.value)
 
        # Shape of output tensor: (batch_size, 768, 512)
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
