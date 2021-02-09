echo -e "\nInstalling Rust tools...\n"

for p in cache expand tree udeps update watch tarpaulin count bloat audit
do
	cargo install cargo-$p
done

echo -e "\nInstalling pip tools...\n"

for p in docker-compose ansible
do
	pip3 install $p
done
