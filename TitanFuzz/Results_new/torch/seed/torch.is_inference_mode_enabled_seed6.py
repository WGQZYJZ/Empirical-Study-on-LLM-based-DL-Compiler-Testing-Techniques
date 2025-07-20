input_data = torch.randn(1, 1, 28, 28)
torch.is_inference_mode_enabled()
input_data.requires_grad_(False)
torch.is_inference_mode_enabled()