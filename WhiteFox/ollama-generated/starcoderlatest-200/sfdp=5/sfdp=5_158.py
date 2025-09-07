
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.attn = torch.nn.Linear(config["dim"], config["num_heads"])
        self.out = torch.nn.Linear(config["dim"] * 3, config["vocab_size"])
 
    def forward(self, x1, x2):
        d_k = config["dim"] // config["num_heads"]
        v = torch.cat([x1, x2, x1*x2], dim=1)
        # v = x1 + x2 * (config['attn_factor'] - 1) / (config['attn_factor'] + 1) 
        qk = torch.einsum('bc,bc->bcd', x1, x2) * d_k  # Compute the dot product of the query and key
        attn_weights = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weights = torch.dropout(attn_weights, dropout_p, True)  # Apply dropout to the softmax output
        outputs = attn_weights @ v
        outputs = outputs.permute([0, 2, 1]).contiguous().view(-1, self.config["dim"]) # [batch size, seq len, model dim] -> [batch size * seq len, model dim]
        outputs = self.attn(outputs) + x2  # Add the attention output of the last layer to the input tensor
        outputs = self.out(outputs)
        return outputs


# Initializing the model
m = Model({
  "dim": 32, 
  "num_heads": 4, 
  "vocab_size": 50
})

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
