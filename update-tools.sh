echo -e "\nUpdating Rust and Rust tools...\n"

rustup update
cargo install-update --all

echo -e "\nCleaning cargo cache...\n"

cargo cache --autoclean

echo -e "\nUpdating pip tools...\n"

for p in docker-compose ansible youtube-dl
do
	pip3 install -U $p
done
