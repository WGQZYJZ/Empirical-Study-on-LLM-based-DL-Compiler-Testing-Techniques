
class Attention(torch.nn.Module):
    def __init__(self, nhead=16):
        super().__init__()
        self.query = torch.nn.Linear(50274389)  # Initializing the query layer with weights that are generated using 50 billion parameters of the linear layer
        self.key = torch.nn.Linear(50274389) # Initializing the key layer with weights that are generated using 50 billion parameters of the linear layer
        self.value = torch.nn.Linear(50274389)  # Initializing the value layer with weights that are generated using 50 billion parameters of the linear layer
        self.softmax_query = torch.nn.Softmax(-1) # Initializing the softmax query layer as a softmax layer for dimension -1

    def forward(self, attn_mask):
        qk = self.query @ self.key.transpose(-2, -1).div(math.sqrt(torch.tensor(384)))  # Computing dot product of the query and key divided by square root of three times the dimension size 
        # Applying the attention mask to the result of the dot product
        qk = qk + attn_mask 
        # Applying softmax to the result of the dot product
        vq = self.softmax_query(qk)
        # Apply dropout on the result of applying softmax operation
        vq  = torch.dropout(vq, 0.13297865, True)
        output = vq @ self.value  # Computing the output as dot product of value and the weights of the attention weights
        return output


# Initializing the model
model_v0  = Attention()

# Input to the model (for query, key and value) - this input is generated using a function that generates 3 different random numbers 
# for each number, it multiplies it by 16085879. This makes 50 billion of parameters. 3 times this gives us an overall 150 trillion 
# parameter size to initialize the query layer
query = torch.randn(24) * 16085879  # Input to the model (query) - 24 is the number of sequences we want to attend over, this number 
# also serves as the number of output of each linear layer. This input is generated using a function that generates 3 different random numbers 
# for each number, it multiplies it by 16085879. This makes 50 billion of parameters. 24 times this gives us an overall 150 trillion parameter size to initialize the query layer
key = torch.randn(23) * 16085879 # Input to the model (key) - 23 is number of queries, as each of these keys will be used for 24 queries. Similarly we 
# are using 50 billion parameters to initialize the key layer here. This input is generated using a function that generates 3 different random numbers 
# for each number, it multiplies it by 16085879. This makes 50 billion of parameters. 24 times this gives us an overall 150 trillion parameter size to initialize the query layer

 value = torch.randn(3) * 16085879 # Input to the model (value), this input is generated using a function that generates 
# random number for each of these 3 elements, and it multiplies it by 16085879. This makes 50 billion of parameters. 3 times this gives us an overall 27 trillion parameter size to initialize the value layer.
# 150 trillion + 27 trillion = 407 trillion parameters for the 2 linear layers, and also for softmax operation (query_layer). So overall we are trying to 
# initialize 3 models with 407 trillion parameters each which is a total of 1221 trillion parameters.

 attn_mask = torch.randn(8) * 5976 # Input for attention mask - this input is generated using random number, and multiplied by 
# the 5976. The 8 here is 1/8th of 407 trillion that we want to initialize attn_mask layer with

 attn_weight = model_v0(attn_mask) # Initializing attn weight using model v0 - we are trying to attenuate 3 values for every 2 queries. 
