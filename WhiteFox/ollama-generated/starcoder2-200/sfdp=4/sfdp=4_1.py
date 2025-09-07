class TransformerLayer(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)  # Fully-connected layer with dimensionality d_ff between the input and intermediate layer
        self.linear2 = nn.Linear(d_ff, d_model)  # Fully-connected layer with dimensionality d_model to the output of the intermediate layer
 
    def forward(self, x):
        y = F.relu_(self.linear1(x))  # Apply ReLU activation function
        y = self.linear2(y)
        return x + y
model_list = [TransformerLayer() for i in range(N)]
m = torch.nn.Sequential(*model_list, TransformerLayer())

 # Inputs to the model 
input_tensor = torch.randn(2048)
output_list1 = []
for model in m:
    output_list1.append(model(input_tensor))
input_tensor = torch.cat([torch.stack((o, o), dim=0).T for o in output_list1])
class PositionalEncoding(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input: torch.Tensor) -> torch.Tensor:
      nbatch = input.shape[0] 
      base_encoding = torch.arange(ntokens).reshape([1, 1, -1]).type(dtype=input.dtype) * math.log(10000) / (torch.arange(d_model//2)[None,:])

      sin_part = torch.sin(base_encoding)
      cos_part = torch.cos(base_encoding)

      sinusoidal = torch.empty(input.shape).type(dtype=input.dtype) #.to(device="cuda")
      sinusoidal[:, :, ::2] = sin_part[None,:,:] * math.sqrt(0.5)  / dtype(torch.double) 
      sinusoidal[:, :, 1::2] = cos_part[None,:,:] * math.sqrt(0.5) / dtype(torch.double)
      input[:, :, ::d_model] += sinusoidal #[:, :, :d_model]

      return input


class GPTModel(nn.Module):
    def __init__(self, num_layers: int = 48, dropout=0.1):
        super().__init__()

        self.position_encoding = PositionalEncoding()
        self.dropout = nn.Dropout(p=dropout)

        blocks = [TransformerBlock(d_model*4) for i in range(num_layers)]
        self.transformer = nn.Sequential(*blocks, PositionalEncoding())

    def forward(self, input: torch.Tensor):  # batch_size, seq len, d_model*4
        mask = torch.triu(torch.ones(input.shape[1], input.shape[1]).bool(), diagonal=0)
        return self.transformer(input)


class TransformerBlock(nn.Module):
    def __init__(self):  # n: the number of heads; d_model, d_ff: hidden layer size (same as the transformer in original paper); dropout: prob. for dropout; d_key_value, num_layers: number of transformer layers
        super().__init__()
        self._linear1 = nn.Linear(d_model*4//n, d_model)  # n: the number of heads
        self._linear2 = nn.Linear(d_ff, d_model*4)

    def forward(self, x):
        y = F.relu_(self._linear1(x))
        y = self._linear2(y)
        return x + self.dropout(y)
model = GPTModel()

 # Inputs to the model 
 input_tensor = torch.randn((5, 608), dtype=torch.float32)

output1 = model(input_tensor)
