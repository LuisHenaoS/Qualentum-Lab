function cd(){
	builtin cd "$@"
	
	if [[ "$1" == ".." || "$1" == "../*" ]]; then
		return 0;
	fi

	autodeps
}

