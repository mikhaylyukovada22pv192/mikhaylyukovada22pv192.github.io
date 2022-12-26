import Axios, {AxiosError} from "axios";

const capabilitiesPath: string = 'http://localhost:8080/capabilities';


export async function getCapabilities() {
    return Axios.get(capabilitiesPath
    ).then
    (response => {
        return response.data;
    })
        .catch((error: AxiosError) => {
            alert(`${error.response!.status} ${error.response!.data}.`);
            return null;
        });
}