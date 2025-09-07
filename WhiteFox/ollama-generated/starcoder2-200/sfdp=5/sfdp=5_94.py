
class Model(torch.nn.Module):
    def __init__(self, hidden=32, num_layers=1):
        super().__init__()
        self.rnn = torch.nn.LSTM(
            input_size=hidden,
            hidden_size=hidden // 4,
            num_layers=num_layers,
            batch_first=True
        )
    def forward(self, x2):
        output3, (state1, state2)  = self.rnn(x2) # RNN with input and hidden size // 4
        return output3
# Initializing the model
model = Model()

 # Inputs to the model
input_size = [64] * 7 + ([1058]) + ([32, 32], [32], [32], [32], [32])
output = model(torch.randn(*input_size))

