
class Model(torch.nn.Module):
    def __init__(self, input_size: int, attention_head: int = 8, num_layers: int = 6):
        super().__init__()

        self.attention_layer = torch.nn.MultiheadAttention(
            input_dim=input_size,
            output_dim=attention_head)
        self.linear = torch.nn.Linear(input_size, 128, bias=True)
        self.batchnorm1d = torch.nn.BatchNorm1d(num_features=input_size*4, eps=0.001, momentum=0.95, affine=True)
        self.activation1d = torch.nn.LeakyReLU()

        self.attention_layer2 = torch.nn.MultiheadAttention(
            input_dim=128,
            output_dim=attention_head)
        self.linear2 = torch.nn.Linear(attention_head, 64, bias=True)
        self.batchnorm2d = torch.nn.BatchNorm1d(num_features=attention_head*4, eps=0.001, momentum=0.95, affine=True)

        for layer in range(num_layers):
            setattr(self, f'layer_{layer}', self._make_stage())

    def _make_stage(self):
        return torch.nn.Sequential(
            torch.nn.Linear(input_size, 128),
            torch.nn.BatchNorm1d(num_features=128, eps=0.001, momentum=0.95, affine=True),
            torch.nn.LeakyReLU(),
        )

    def forward(self, x):

        # attention: [batch_size, len(query), num_attention_heads * num_attention_head_dim] @ [batch_size, num_attention_heads * num_attention_head_dim, len(key)] = [batch_size, len(query), len(key)]
        # context: [batch_size, len(query), hidden_size * num_attention_heads * num_attention_head_dim] @ [batch_size, num_attention_heads * num_attention_head_dim, 128] = [batch_size, len(query), 128]
        attention, context = self.attention_layer(
            query=x, key=x, value=x)

        # (batch_size * len(query)) @ (num_attention_head * num_attention_head_dim) = [batch_size * len(query)] * 4 = [batch_size * len(query), 64]
        x1 = self.linear(self.activation1d(context)).view(-1, 128).transpose(0, 1)

        # (batch_size * len(query)) @ (num_attention_head * num_attention_head_dim) = [batch_size * len(query)] * 4 = [batch_size * len(query), attention_head]
        x2 = self.linear2(self.activation1d(
            torch.nn.MultiheadAttention(
                input_dim=x1,
                output_dim=attention_head).forward(context, context, context)[0])).view(-1, attention_head)

        # (batch_size * len(query)) @ (num_attention_head * num_attention_head_dim) = [batch_size * len(query)] * 4 = [batch_size * len(query), attention_head]
        x3 = self.linear2(self.activation1d(
            torch.nn.MultiheadAttention(
                input_dim=x1,
                output_dim=attention_head).forward(context, context, context)[0])).view(-1, attention_head)

        # (batch_size * len(query)) @ (num_attention_head * num_attention_head_dim) = [batch_size * len(query)] * 4 = [batch_size * len(query), attention_head]
        x4 = self.linear2(self.activation1d(
            torch.nn.MultiheadAttention(
                input_dim=x1,
                output_dim=attention_head).forward(context, context, context)[0])).view(-1, attention_head)

        # (batch_size * len(query)) @ (num_attention_head * num_attention_head_dim) = [batch_size * len(query)] * 4 = [batch_size * len(query), attention_head]
        x5 = self.linear2(self.activation1d(
            torch.nn.MultiheadAttention(
                input_dim=x1,
                output_dim=attention_head).forward(context, context, context)[0])).view(-1, attention_head)

        # (batch_size * len(query)) @ (num_attention_head * num_attention_head_dim) = [batch_size * len(query)] * 4 = [batch_size * len(query), attention_head]
        x6 = self.linear2(self.activation1d(
            torch.nn.MultiheadAttention(
                input_dim=x1,
                output_dim=attention_head).forward(context, context, context)[0])).view(-1, attention_head)

        # (batch_size * len(query)) @ (num_attention_head * num_attention_head : : :


##
#@functionfunctionfunctionfunction
#
#defdefdefdefdefdefdefdefdefdefdefdefdefdef
class BloomClientFactory:

    