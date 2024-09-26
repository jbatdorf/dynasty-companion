export default function Home() {
    return (
        <>
            <h1>Enter your league ID to get started.</h1>
            <label id="league-id">
                Enter league id
                <input
                    id="league-id"
                    value={"enter your MFL league id"}
                ></input>
            </label>
            <button
                onClick={() => {
                    console.log("among us");
                }}
            >
                Go!
            </button>
        </>
    );
}
