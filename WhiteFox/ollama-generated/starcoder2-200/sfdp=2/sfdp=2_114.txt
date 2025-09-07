

model_input = torch.randn(2048)

model_output = m(model_input, torch.nn.Parameter())

# Initializing the model
m  = torch.nn.LSTM(350,64, batch_first=True, dropout=.2)


# Input to the model
model_input = torch.randn(19,78)

