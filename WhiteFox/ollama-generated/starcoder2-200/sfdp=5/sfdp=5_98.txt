
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, n_head=128, d_model=768, dropout=0., attn_mask=None):
        super().__init__()
 
        self.n_head = n_head
        self.d_model = d_model
        self.attn_mask  = attn_mask
 
        # Initialize the weights
        self._initialize()
 
    def forward(self, query, key, value):
        # Shape: batch size x head number x sequence length (sequence length) x model dimension for each head
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        if self.attn_mask is not None:
            # Make sure the mask has the right shape. Unsqueeze and squeeze are used to make the shapes match.
            qk  = qk + torch.unsqueeze(self.attn_mask, dim=0) @ torch.unsqueeze(self.attn_mask, dim=-1)
        qk  = self.dropout(torch.softmax(qk, dim=-1))
        # Shape: batch size x head number x sequence length (sequence length) x model dimension for each head
        output  = qk @ value
        return output
 
    def _initialize(self):
        for i in range(self.n_head):
            self.weights['query'].append(torch.nn.Parameter(torch.empty((1, self.d_model), requires_grad=True)))
            self.weights['key'].append(torch.nn.Parameter(torch.empty((1, self.d_model), requires_grad=True)))
            self.weights['value'].append(torch.nn.Parameter(torch.empty((1, self.d_model), requires_grad=True)))
 
def initialize_weights(module):
    for name in module._modules:
        if (name  == 'query' or
                name  == 'key' or 
                name  == 'value'):
            if name  != 'attn':
                initialize_weights(module[name])
            else:
                for i, w in enumerate(module.weights):
                    nn.init.kaiming_uniform_(w)
        elif isinstance(module._modules[name], torch.nn.Linear):
            module._modules[name].weight.data  = F.normalize(module._modules[name].weight.data)
            # Set the bias of each hidden layer to be zero so that we don't need to learn it from the data.
            if module._modules[name].bias is not None:
                nn.init.zeros_(module._modules[name].bias.data)


# Initializing the model and its parameters
model = MultiHeadAttention(n_head=128, d_model=768)  # This is the original implementation for multi head attention.
initialize_weights(model)
 
# Inputs to the model. The query tensor has shape [batch size x sequence length (sequence length) x model dimension]
q = torch.randn([128, 500, 768]) # This is a random tensor of shape [batch size x sequence length (sequence length) x model dimension].
k = torch.randn([128, 500, 768]) # This is also a random tensor of the same shape as q above. 
v = torch.randn([128, 500, 768]) # This is also another random tensor of the same shape as k and q. 
 
# Run inference. This will add gradients to the query, key, value tensors. The shape should be [batch size x head number x sequence length (sequence length) x model dimension for each head].
